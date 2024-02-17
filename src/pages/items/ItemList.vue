<template>
    <base-dialog :show="!!error" title="An error occured!" @close="handleError">
      <p>{{ error }}</p>
    </base-dialog>
    <section>
      <base-card>
        <div class="controls">
          <base-button mode="outline" @click="loadCoaches(true)">Refresh</base-button>
        </div>
  
        <div v-if="isLoading">
          <base-spinner></base-spinner>
        </div>
  
        <ul v-else-if="hasItems">
          <grocery-item
            v-for="item in allItems"
            :key="item.id"
            :id="item.id"
            :itemName="item.itemName"
            :rate="item.rate"
            :quantity="item.quantity"
            :category="item.category"
          ></grocery-item>
        </ul>
        <h2 v-else>No items Found</h2>
      </base-card>
    </section>
  </template>
  
  <script>
  import GroceryItem from '../../components/items/GroceryItem.vue';
  
  export default {
    components: {
      GroceryItem,
    },
    data() {
      return {
        isLoading: false,
        error: null
      };
    },
  
    computed: {
      isLoggedIn(){
        return this.$store.getters.isAuthenticated;
      },
      allItems() {
        return this.$store.getters['items/items'];
      },
      hasItems() {
        return !this.isLoading && this.$store.getters['items/hasItems'];
      },
    },
    methods: {
      handleError(){
        this.error = null
      },
      async loadCoaches(refresh = false){
        this.isLoading = true
        try{
        await this.$store.dispatch('items/loadCoaches', {forceRefresh: refresh})
        } catch(error){
          this.error = error.message || 'Something went wrong'
        }
        this.isLoading = false
      }
    },
    created(){
      this.loadCoaches()
    }
  };
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