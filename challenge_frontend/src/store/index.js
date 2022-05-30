import { createStore } from "vuex";
import { http } from "@/axios/axios.js";
import VueCookies from "vue-cookies";

export default createStore({
  state: {
    user: null,
  },
  mutations: {},
  getters: {
    loggedIn() {
      return VueCookies.get("accessToken", "refreshToken") != null;
    },
  },
  actions: {
    userLogout() {
      http
        .post("/api/token/blacklist/", {
          access: VueCookies.get("accessToken"),
          refresh: VueCookies.get("refreshToken"),
        })
        .then(() => {
          VueCookies.set("accessToken", "").set("refreshToken", "");
        })
        .catch(() => {});
    },
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        http
          .post("/api/token/", {
            email: usercredentials.email,
            password: usercredentials.password,
          })
          .then((response) => {
            VueCookies.set("accessToken", response.data.access).set(
              "refreshToken",
              response.data.refresh
            );
            resolve();
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
  },
  modules: {},
});
