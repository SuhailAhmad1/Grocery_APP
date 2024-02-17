export default {
    registerCoach(state, payload){
        state.items.push(payload);
    },
    setCoaches(state, payload){
        state.items = payload
    },
    setFetchTimeStamp(state){
        state.lastFetch = new Date().getTime();
    }
};