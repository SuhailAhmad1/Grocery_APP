import mutations from './mutations.js'
import actions from './actions.js'
import getters from './getters.js'

export default {
    namespaced: true,
    state() {
        return {
            lastFetch: null,
            items: [
                {
                    itemName: "Curd",
                    rate: "26",
                    quantity: 100,
                    category: ["fruits_and_vegetables", "dairy"],
                    id: 1
                },
                {
                    itemName: "Chicken",
                    rate: "300",
                    quantity: 45,
                    category: ["fruits_and_vegetables", "meat_and_chicken"],
                    id: 2
                },
                {
                    itemName: "Butter Milk",
                    rate: "10",
                    quantity: 12,
                    category: ["dairy"],
                    id: 3
                }
            ]
        }
    },
    mutations,
    actions,
    getters
}