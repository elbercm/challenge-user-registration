<template>
  <nav
    class="top-0 absolute z-50 w-full flex flex-wrap items-center justify-end px-2 py-3 navbar-expand-lg"
  >
    <div class="container px-4 mx-auto flex flex-wrap items-center justify-end">
      <div
        class="w-full relative flex justify-end lg:w-auto lg:static lg:block lg:justify-start"
      >
        <router-link
          class="text-white text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
          to="/"
        >
          Home
        </router-link>

        <router-link
          v-if="this.loggedIn"
          class="text-white text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
          to="/admin/profile"
        >
          Perfil
        </router-link>

        <a
          v-if="this.loggedIn"
          href=""
          class="text-white text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
          @click.prevent="logout"
        >
          Logout
        </a>
      </div>
    </div>
  </nav>
</template>
<script>
import store from "@/store";
export default {
  data() {
    return {
      loggedIn: false,
    };
  },
  mounted() {
    this.loggedIn = store.getters.loggedIn;
  },

  methods: {
    logout() {
      store.dispatch("userLogout").then(() => {
        this.$router.push("/auth");
      });
    },
  },
};
</script>
