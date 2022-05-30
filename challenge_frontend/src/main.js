import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

// vuex
import store from "@/store/index.js";

// Toast
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

// styles
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";

import App from "@/App.vue";
import Index from "@/views/Index.vue";

// layouts
import Auth from "@/layouts/Auth.vue";

// views for Admin layout
import Profile from "@/views/admin/Profile.vue";

// views for Auth layout
import Login from "@/views/auth/Login.vue";
import Register from "@/views/auth/Register.vue";

// Axios
import axios from "axios";

// Cookies
import VueCookies from "vue-cookies";

const routes = [
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/",
        name: "/",
        component: Index,
      },
      {
        path: "/auth/login",
        name: "login",
        component: Login,
      },
      {
        path: "/auth/register",
        component: Register,
      },
      {
        path: "/admin/profile",
        name: "profile",
        component: Profile,
        meta: {
          requiresLogin: true,
        },
      },
    ],
  },

  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: "/" });
    } else {
      next();
    }
  } else {
    next();
  }
});

createApp(App)
  .use(router, VueSweetalert2, axios, store, VueCookies, {
    expire: "1d",
    sameSite: "Lax",
  })
  .mount("#app");
