from app.models.document import Document
from app import db
import traceback
import json
import time
from werkzeug.utils import secure_filename
import os
import datetime

class UserService():
    def upload_doc(self, userid, files):
        backend_path = []
        current_time_stamp = str(time.time()).replace('.','')
        for doc in files.getlist('doc'):
            if doc:
                docname = secure_filename(doc.filename)
                if check_duplicates(docname, userid):
                    return False, "File already exists"
            else:
                print("DOC NAME ISSUE")
                return False, "Invalid File type or filename"
            try:
                if not os.path.isdir(f"{DOWNLOAD_DIR}{userid}"):
                    os.mkdir(f"{DOWNLOAD_DIR}{userid}")
                if not os.path.isdir(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}"):
                    os.mkdir(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}")
                filepath = os.path.join(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}", docname)
                status, filepath = handle_duplicate_docname(filepath, docname)
                if status:
                    doc.save(os.path.join(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}", docname))
                    backend_path.append(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}/{docname}")
                    path = f"{MODEL_EFS_PATH}{userid}/{current_time_stamp}/{docname}"
                    # check file extensions and call pdfconverter in backend.
                else:
                    path = filepath
                    doc.save(path)
                    backend_path.append(f"{DOWNLOAD_DIR}{userid}/{current_time_stamp}/{docname}")

                data = {
                "user_id": userid,
                "status": "created",
                "is_active": True,
                "timeTaken": 0,
                "created_at": datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
                "doc_path": backend_path,
                "is_edited": False,
                "edited_at": datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
                }
                status = create_process(data, userid)
                if status:
                    return True, "Successfully uploaded"
                else:
                    return False, "Failed while saving to the DB"
            except Exception as e:
                print("Upload_file exception", e)
                return False, "Something went wrong"
            
    def handle_duplicate_docname(filepath, docname):
        '''
        check if file path is duplicated,
        if it is append numric string and genrate a new path.
        '''
        try:
            if not os.path.isfile(filepath):
                return True, filepath
            else:
                print("DUPLICATE NAME FOUND")
                count = 0
                create_path = filepath
                while(os.path.isfile(create_path)):
                    count += 1
                    extension = docname.split(".")[-1]
                    doc_name = docname.split(".")[:-1]
                    name_str = " ".join(doc_name)
                    print("name_string", name_str)
                    name_str += f"_{count}"
                    name = f"{name_str}.{extension}"
                    part1 = create_path.split("/")[:-1]
                    part1_str = "/".join(part1)
                    create_path = os.path.join(part1_str, name)
                print("FILEPATH FROM DUPLICATE_DOCNAME", create_path)
                return False, create_path
        except Exception as e:
            print(traceback.format_exec(), e)

def check_duplicates(doc_name, user_id):
    docs = get_all_processess(user_id)
    for doc in docs:
        if doc_name == doc["doc_path"][0].split("/")[-1]:
            return True
        
    def create_new_doc(self, data):
        try:
            new_doc = Document(
                user_id = data["user_id"],
                doc_path = json.dumps(data["doc_path"]),
                output = "",
            )
            db.session.add(new_doc)
            db.session.commit()
            return True
        except Exception as e:
            print(traceback.print_exc(e))
            return False
        