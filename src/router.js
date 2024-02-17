import { createRouter, createWebHistory } from "vue-router";

import ItemList from "./pages/user_pages/items/ItemList.vue"
import AddCart from "./pages/user_pages/cart/AddCart.vue"
import CartList from "./pages/user_pages/cart/CartList.vue"
import NotFound from './pages/NotFound.vue';

import ManagerItem from "./pages/manager_pages/ManagerItem.vue"
import EditItem from "./pages/manager_pages/EditItem.vue"
import AddItem from './pages/manager_pages/AddItem.vue'
// import CoachDetail from './pages/coaches/CoacheDetail.vue';
// import CoachesList from './pages/coaches/CoachesList.vue';
// import CoachRegistration from './pages/coaches/CoachRegistration.vue';
// import ContactCoach from './pages/requests/ContactCoach.vue';
// import RequestsRecieved from './pages/requests/RequestsRecieve.vue';
// import UserAuth from "./pages/auth/UserAuth.vue"
// import store from './store/index.js'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            redirect: '/home',
            meta: { requiresAuth: true }
        },
        {
            path: '/home',
            component: ItemList,
            meta: { requiresAuth: true }
        },
        {
            path: '/items/:id/add_to_cart',
            component: AddCart,
            props: true,
            meta: { requiresAuth: true },
        },
        {
            path: '/cart',
            component: CartList,
            meta: { requiresAuth: true }
        },
    //     {
    //         path: '/auth',
    //         component: UserAuth,
    //         meta: { requiresUnauth: true }
    //     },

        // Manager Routes
        {
            path: '/home/manager',
            component: ManagerItem,
            meta: { requiresAuth: true }
        },
        {
            path: '/manager/:id/edit',
            component: EditItem,
            props: true,
            meta: { requiresAuth: true }
        },
        {
            path: '/manager/addItem',
            component: AddItem,
            meta: { requiresAuth: true }
        },

        {
            path: '/:notFound(.*)',
            component: NotFound
        }
    ]
});

// router.beforeEach(function (to, from, next) {
//     if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
//         next('/auth')
//     } else if (to.meta.requiresUnauth && store.getters.isAuthenticated) {
//         next("/coaches")
//     }
//     else {
//         next()
//     }
// })

export default router;