export default({
    editManagerItem(state, payload){
        const index = state.manager_items.findIndex(item => item.id == payload.id);
        state.manager_items[index] = payload
        console.log(state.manager_items)
    },
    addItem(state, payload){
        state.manager_items.push(payload)
    },
    deleteItem(state, payload){
        const indexToDelete = state.manager_items.findIndex(item => item.id === payload.id);
        state.manager_items.splice(indexToDelete, 1);
    }
})