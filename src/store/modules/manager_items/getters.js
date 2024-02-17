export default({
    managerItems(state){
        return state.manager_items;
    },

    hasItem(state){
        return state.manager_items.length !== 0;
    }
})