<template>
    <base-dialog :show="!!error" title="An error occured!" @close="handleError">
        <p>{{ error }}</p>
    </base-dialog>
    <section>
        <base-card>
            <div class="controls">
                <base-button mode="outline" link :to="addItem">Add Item</base-button>
            </div>

            <div v-if="isLoading">
                <base-spinner></base-spinner>
            </div>

            <ul v-else-if="hasItems">
                <manager-item v-for="item in allManagerItems" :key="item.id" :id="item.id" :itemName="item.itemName"
                    :rate="item.rate" :quantity="item.quantity" :category="item.category"></manager-item>
            </ul>
            <h2 v-else>No items Found</h2>
        </base-card>
    </section>
</template>

<script>
import ManagerItem from '../../components/items/ManagerItem.vue';

export default ({
    components: {
        ManagerItem
    },
    data() {
        return {
            isLoading: false,
            error: null
        };
    },
    computed: {
        allManagerItems() {
            return this.$store.getters['manager_items/managerItems']
        },
        hasItems() {
            return this.$store.getters['manager_items/hasItem']
        },
        addItem() {
            return "/manager/addItem"
        }
    }
})
</script>

<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.controls {
  display: flex;
  justify-content: space-between;
}
</style>