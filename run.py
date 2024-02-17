from app import create_app
from app.routes.auth_routes import auth_routes
from app.routes.user_routes import user_routes

# Create the Flask app using the application factory
app = create_app()

# Registering the route 
app.register_blueprint(auth_routes)
app.register_blueprint(user_routes)
if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
