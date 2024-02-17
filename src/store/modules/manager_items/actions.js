export default({
    editItem(context, payload){
        context.commit('editManagerItem', payload)
    },
    addItem(context, payload){
        context.commit('addItem', payload)
    },
    deleteItem(context, payload){
        context.commit('deleteItem', payload)
    }
})