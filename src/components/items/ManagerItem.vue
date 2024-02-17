<template>
  <li>
    <h3>{{ itemName }}</h3>
    <h4>Rate : Rs. {{ rate }}</h4>
    <h5>Quantity Available : {{ quantity }}</h5>
    <div>
      <base-badge v-for="cat in category" :key="cat" :type="cat" :title="cat"></base-badge>
    </div>
    <div class="actions">
      <base-button link :to="editItem">Edit</base-button>
      <base-button mode="red" @click="deleteItem()">Delete</base-button>
    </div>
  </li>
</template>

<script>
export default {
  props: ["id", "itemName", "rate", "quantity", "category"],
  methods: {
    deleteItem() {
      this.$store.dispatch('manager_items/deleteItem',{
        id: this.id
      })
    }
  },
  computed: {
    fullName() {
      return this.firstName + " " + this.lastName;
    },
    editItem() {
      return "/manager/" + this.id + "/edit";
    }
  }
}
</script>

<style scoped>
li {
  margin: 1rem 0;
  border: 1px solid #424242;
  border-radius: 12px;
  padding: 1rem;
}

h3 {
  font-size: 1.8rem;
}

h3,
h4 {
  margin: 0.5rem 0;
}

div {
  margin: 0.5rem 0;
}

.actions {
  display: flex;
  justify-content: flex-end;
}
</style>