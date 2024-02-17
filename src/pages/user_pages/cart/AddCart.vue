<template>
    <base-card>
        <h3>Item Name : {{ item_name }}</h3>
        <h4>Rate : Rs. {{ item_rate }}</h4>
        <h5>Quantity Available : {{ item_quantity }}</h5>
    </base-card>
    <base-card>
        <form @submit.prevent="submitForm">
            <div class="form-control">
                <label for="quantity">Quanitity</label>
                <input type="number" id="item_quantity" v-model.number="buy_quantity">
            </div>
            <div class="form-control">
                <label for="message">Additional Instructions</label>
                <textarea id="message" rows="5" v-model.trim="notes"></textarea>
            </div>
            <p class="errors" v-if="!formIsValid">Please enter valid data.</p>
            <div class="actions">
                <h3>Total Amount : Rs. {{ total_amount }}</h3>
                <base-button>Add to Cart</base-button>
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
            buy_quantity: null,
            total_amount: 0,
            notes: '',
            formIsValid: true
        }
    },
    watch: {
        buy_quantity(){
            this.total_amount = this.buy_quantity * this.item_rate;
        }
    },
    methods: {
        submitForm() {
            this.formIsValid = true;
            if (this.buy_quantity === 0  || this.notes === '' || this.buy_quantity > this.item_quantity) {
                console.log("error...")
                this.formIsValid = false;
                return;
            }
            this.$store.dispatch('cart/addToCart', {
                item_id: this.item_id,
                item_name: this.item_name,
                quantity: this.buy_quantity,
                item_rate: this.item_rate,
                total_amount: this.total_amount
            })
            this.$router.replace("/home")
        },
        get_item_info() {
            const items = this.$store.getters['items/items'];
            const item = items.find(it => it.id == this.id);
            console.log(item)
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
    text-align: center;
    display: flex;
    justify-content: space-between;
}
</style>