<template>
    <base-card>
    <h3>Edit Item</h3>
        <form @submit.prevent="submitForm">
            <div class="form-control">
                <label for="item_name">Item name</label>
                <input type="text" id="item_name" v-model="item_name">
            </div>
            <div class="form-control">
                <label for="item_rate">Item rate (Rs.)</label>
                <input type="number" id="item_quantity" v-model="item_rate">
            </div>
            <div class="form-control">
                <label for="item_quantity">Quanitity</label>
                <input type="number" id="item_quantity" v-model.number="item_quantity">
            </div>
            <div class="form-control check_box">
                <label for="item_category">Category</label>
                <input type="checkbox" value="Fruits and Vegetables" id="item_category" v-model="category"> Fruits and Vegetables
                <input type="checkbox" value="Meat And Chicken" id="item_category" v-model="category"> Meat And Chicken
                <input type="checkbox" value="Dairy" id="item_category" v-model="category"> Dairy
            </div>
            <p class="errors" v-if="!formIsValid">Please enter valid data.</p>
            <div class="actions">
                <base-button>Update</base-button>
            </div>
        </form>
    </base-card>
</template>

<script>
export default {
    props: ["id"],
    data() {
        return {
            item_id: 0,
            item_name: '',
            item_rate: 0,
            item_quantity: 0,
            category: [],
            formIsValid: true
        }
    },
    methods: {
        submitForm() {
            this.formIsValid = true;
            if (this.item_quantity === 0  || this.item_name === '' || this.item_rate <=0 || this.category.length === 0) {
                console.log("error...")
                this.formIsValid = false;
                return;
            }
            this.$store.dispatch('manager_items/editItem', {
                id: this.item_id,
                itemName: this.item_name,
                quantity: this.item_quantity,
                rate: this.item_rate,
                category: this.category
            })
            this.$router.replace("/manager/home")
        },
        get_item_info() {
            const items = this.$store.getters['manager_items/managerItems'];
            const item = items.find(it => it.id == this.id);
            if (item) {
                this.item_id = this.id;
                this.item_name = item.itemName;
                this.item_rate = item.rate;
                this.item_quantity = item.quantity;
                return true;
            } 
            return false
        }
    },
    created(){
        this.get_item_info();
    }
}
</script>

<style scoped>
form {
    margin: 1rem;
    border: 1px solid #ccc;
    border-radius: 12px;
    padding: 1rem;
}

.form-control {
    margin: 0.5rem 0;
}

label {
    font-weight: bold;
    margin-bottom: 0.5rem;
    display: block;
}

input,
textarea {
    display: block;
    width: 100%;
    font: inherit;
    border: 1px solid #ccc;
    padding: 0.15rem;
}

input:focus,
textarea:focus {
    border-color: #3d008d;
    background-color: #faf6ff;
    outline: none;
}

.errors {
    font-weight: bold;
    color: red;
}

.actions {
    display: flex;
    justify-content: flex-end;
}

h3{
    text-align: center;
    font-size: 1.5rem;
    color: rgb(21, 31, 15);
}

</style>