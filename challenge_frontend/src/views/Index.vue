<template>
  <div class="flex content-center items-center justify-center h-full">
    <div class="w-full lg:w-6/12 px-4">
      <div
        class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
      >
        <div v-if="!this.loggedIn" class="rounded-t bg-white mb-0 px-6 py-6">
          <div class="text-center flex justify-center">
            <h6 class="text-blueGray-700 text-xl font-bold">
              Olá Visitante, seja bem-vindo ao meu site! <br />
              Faça seu login ou cadastre-se para continuar.
            </h6>
          </div>
          <div class="text-center flex justify-center mt-5">
            <router-link
              class="bg-emerald-500 text-white active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150 mr-4"
              type="button"
              to="/auth/login"
            >
              LogIn
            </router-link>
            <router-link
              class="bg-emerald-500 text-white active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
              type="button"
              to="/auth/register"
            >
              Criar conta!
            </router-link>
          </div>
        </div>
        <!-- Usuário esta logado -->
        <div
          v-if="this.loggedIn == true"
          class="rounded-t bg-white mb-0 px-6 py-6"
        >
          <div class="text-center flex justify-center">
            <h6 class="text-blueGray-700 text-xl font-bold">
              Olá {{ this.usuario.name }}, seja bem-vindo! <br />
            </h6>
          </div>
          <div class="text-center flex justify-center mt-5">
            <router-link
              class="bg-indigo-500 text-white active:bg-indigo-500 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150 mr-4"
              type="button"
              to="/admin/profile"
            >
              Atualizar Perfil
            </router-link>
            <button
              class="bg-red-600 text-white active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
              type="button"
              @click="deleteUser"
            >
              Excluir conta!
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { http } from "@/axios/axios.js";
import VueCookies from "vue-cookies";
import store from "@/store";
import Swal from "sweetalert2";

export default {
  name: "Home",

  data() {
    return {
      usuario: {},
      loggedIn: false,
    };
  },
  mounted() {
    this.getUser();
    this.loggedIn = store.getters.loggedIn;
    window.scrollTo(0, 0);
  },
  created() {},
  methods: {
    // Dados do Usuário Logado
    getUser() {
      http
        .get("/api/v1/user/", {
          headers: { Authorization: `Bearer ${VueCookies.get("accessToken")}` },
        })
        .then((response) => {
          this.usuario = response.data;
          this.usuario.name = this.usuario.usuario.name;
        })
        .catch(() => {});
    },
    // Exclusão do Usuário Logado
    deleteUser() {
      Swal.fire({
        title: "Excluir Conta?",
        text: "Não é possível reverter essa ação!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "SIM, Excluir Conta!",
        cancelButtonText: "Não excluir",
      }).then((result) => {
        if (result.isConfirmed) {
          http
            .delete("/api/v1/delete-user", {
              headers: {
                Authorization: `Bearer ${VueCookies.get("accessToken")}`,
              },
            })
            .then(() => {
              store.dispatch("userLogout").then(() => {
                this.$router.push("/auth");
              });
            })
            .catch(() => {});
        }
      });
    },
  },
};
</script>
