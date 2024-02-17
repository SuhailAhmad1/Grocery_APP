<template>
    <base-dialog :show="!!error" title="An error occured!" @close="handleError">
        <p>{{ error }}</p>
    </base-dialog>
    <section>
        <base-card>
            <header>
                <h2>Cart Items</h2>
            </header>
            <div v-if="isLoading">
                <base-spinner></base-spinner>
            </div>
            <h3 v-else-if="!get_cart_items.length">You haven't recieved any requests yet!</h3>
            <ul v-else-if="!isLoading">
                <base-card v-for="item in get_cart_items" :key="item.id">
                    <h3>Item : {{ item.item_name }}</h3>
                    <h5>Quantity : {{ item.quantity }}</h5>
                    <h5>Rate : {{ item.item_rate }}</h5>
                    <h5>Amount : {{ item.total_amount }}</h5>
                </base-card>
            </ul>
        <div v-if ="get_cart_items.length" class="actions">
            <h3>Grand Total : {{ total_amount }}</h3>
            <base-button>Buy All</base-button>
        </div>
        
        </base-card>
    </section>
</template>
  
<script>

export default {
    data() {
        return {
            isLoading: false,
            error: null,
        };
    },
    computed: {
        get_cart_items() {
            return this.$store.getters['cart/cart_items'];
        },
        total_amount(){
            return 100
        }
    }
};
</script>
  
<style scoped>
header {
    text-align: center;
}

ul {
    list-style: none;
    margin: 2rem auto;
    padding: 0;
    max-width: 30rem;
}

h3, h5 {
    text-align: center;
}
.actions {
  display: flex;
  justify-content: space-between;
}
</style>