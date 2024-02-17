export default {
    async addToCart(context, payload){
        context.commit('addRequest',payload)
    }
};