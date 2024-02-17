export default {
    async registerCoach(context, payload) {
        const userId = context.rootGetters.userId;
        const new_item = {
            itemName: payload.first,
            description: payload.desc,
            rate: payload.rate,
            areas: payload.areas
        };
        context.commit('registerCoach', {
            ...new_item,
            id: userId
        })
    },
    async loadCoaches(context, payload) {
        if (!payload.forceRefresh && !context.getters.shouldUpdate){
            return;
        }
    }
};