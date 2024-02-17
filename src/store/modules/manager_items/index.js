import mutations from "./mutations"
import actions from "./actions"
import getters from "./getters"

export default({
    namespaced: true,
    state(){
        return {
            lastFetch: null,
            manager_items: [
                {
                    itemName: "Curd",
                    rate: "26",
                    quantity: 100,
                    category: ["fruits_and_vegetables", "dairy"],
                    id: 1
                },
                {
                    itemName: "Chicken",
                    rate: "260",
                    quantity: 145,
                    category: ["meat", "dairy"],
                    id: 2
                }
            ]
        }
    },
    mutations,
    actions,
    getters
})