import { createStore } from "vuex";

import itemModule from './modules/items/index.js'
import cartModule from "./modules/cart/index.js";
import authModule from './modules/auth/index.js'

const store = createStore({
    modules: {
        items: itemModule,
        cart: cartModule,
        auth: authModule
    }
})

export default store;