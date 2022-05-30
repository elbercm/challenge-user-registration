<template>
  <div
    class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
  >
    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">Meus dados</h6>
        <button
          class="bg-red-500 text-white active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
          type="button"
          @click="deleteUser"
        >
          Excluir conta
        </button>
      </div>
    </div>
    <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
      <form @submit.prevent="updateUserSubmit">
        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          Meus Dados
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Nome
                <small
                  v-if="submitted && v$.usuario.name.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Nome é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.name"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Email
                <small
                  v-if="submitted && v$.usuario.email.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  E-mail inválido*
                </small>
              </label>
              <input
                type="email"
                disabled="disabled"
                class="border-0 px-3 py-3 text-blueGray-600 bg-blueGray-200 rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.email"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                CPF
                <small
                  v-if="submitted && v$.usuario.cpf.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  CPF é requerido*
                </small>
                <small
                  v-if="submitted && v$.usuario.cpf.cpfValid.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Número do CPF inválido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.cpf"
                v-maska="'###.###.###-##'"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                PIS
                <small
                  v-if="submitted && v$.usuario.pis.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  PIS é requerido*
                </small>
                <small
                  v-if="submitted && v$.usuario.pis.pisValid.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Número do PIS inválido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.pis"
                v-maska="'###.#####.##-#'"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          Meu Endereço
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Endereço
                <small
                  v-if="submitted && v$.usuario.endereco.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Endereço é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.endereco"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Numero
                <small
                  v-if="submitted && v$.usuario.numero.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Número é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.numero"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Complemento
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.complemento"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                for="estado"
              >
                Estado
                <small
                  v-if="submitted && v$.usuario.estado.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Estado é requerido*
                </small>
              </label>
              <select
                v-model="usuario.estado"
                class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              >
                <option>São Paulo</option>
                <option>Acre</option>
                <option>Alagoas</option>
                <option>Amapá</option>
                <option>Amazonas</option>
                <option>Bahia</option>
                <option>Ceará</option>
                <option>Distrito Federal</option>
                <option>Espírito Santo</option>
                <option>Goiás</option>
                <option>Maranhão</option>
                <option>Mato Grosso</option>
                <option>Mato Grosso do Sul</option>
                <option>Minas Gerais</option>
                <option>Pará</option>
                <option>Paraíba</option>
                <option>Paraná</option>
                <option>Pernambuco</option>
                <option>Piauí</option>
                <option>Rio de Janeiro</option>
                <option>Rio Grande do Norte</option>
                <option>Rio Grande do Sul</option>
                <option>Rondônia</option>
                <option>Roraima</option>
                <option>Santa Catarina</option>
                <option>Sergipe</option>
                <option>Tocantins</option>
              </select>
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Município
                <small
                  v-if="submitted && v$.usuario.municipio.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Município é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.municipio"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Bairro
                <small
                  v-if="submitted && v$.usuario.bairro.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  Bairro é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.bairro"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                CEP
                <small
                  v-if="submitted && v$.usuario.cep.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  CEP é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.cep"
                v-maska="'#####-###'"
              />
            </div>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                Pais
                <small
                  v-if="submitted && v$.usuario.pais.required.$invalid"
                  class="font-bold leading-normal mt-0 mb-4 text-red-500"
                >
                  País é requerido*
                </small>
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model="usuario.pais"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />
        <div class="rounded-t mb-0 px-6 py-6">
          <div class="text-right">
            <button
              class="bg-indigo-500 text-white active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
            >
              Atualizar dados
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import VueCookies from "vue-cookies";
import { maska } from "maska";
import { required } from "@vuelidate/validators";
import { pisValid, cpfValid } from "@/plugins/utils";
import useVuelidate from "@vuelidate/core";
import { http } from "@/axios/axios.js";
import store from "@/store";
import Swal from "sweetalert2";

const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener("mouseenter", Swal.stopTimer);
    toast.addEventListener("mouseleave", Swal.resumeTimer);
  },
});
export default {
  directives: { maska },
  setup() {
    return { v$: useVuelidate() };
  },
  data() {
    return {
      usuario: {
        name: "",
        email: "",
        cpf: "",
        pis: "",
        endereco: "",
        numero: "",
        estado: "",
        complemento: "",
        municipio: "",
        bairro: "",
        cep: "",
        pais: "",
      },
      submitted: false,
    };
  },
  mounted() {
    this.getUser();
    window.scrollTo(0, 0);
  },
  validations() {
    return {
      usuario: {
        name: {
          required,
        },
        email: { required },
        cpf: { required, cpfValid },
        pis: { required, pisValid },
        endereco: { required },
        numero: { required },
        estado: { required },
        municipio: { required },
        bairro: { required },
        cep: { required },
        pais: { required },
      },
    };
  },
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
          this.usuario.email = this.usuario.usuario.email;
          this.usuario.cpf = this.usuario.usuario.cpf;
          this.usuario.pis = this.usuario.usuario.pis;
          this.usuario.endereco = this.usuario.usuario.endereco;
          this.usuario.numero = this.usuario.usuario.numero;
          this.usuario.complemento = this.usuario.usuario.complemento;
          this.usuario.estado = this.usuario.usuario.estado;
          this.usuario.bairro = this.usuario.usuario.bairro;
          this.usuario.municipio = this.usuario.usuario.cidade;
          this.usuario.cep = this.usuario.usuario.cep;
          this.usuario.pais = this.usuario.usuario.pais;
        })
        .catch(() => {});
    },

    // Update do Usuário Logado
    updateUserSubmit() {
      this.submitted = true;

      if (!this.v$.$invalid) {
        const formData = new FormData();
        formData.append("name", this.usuario.name);
        formData.append("email", this.usuario.email);
        formData.append("cpf", this.usuario.cpf);
        formData.append("pis", this.usuario.pis);
        formData.append("endereco", this.usuario.endereco);
        formData.append("numero", this.usuario.numero);
        formData.append("estado", this.usuario.estado);
        formData.append("complemento", this.usuario.complemento);
        formData.append("cidade", this.usuario.municipio);
        formData.append("bairro", this.usuario.bairro);
        formData.append("cep", this.usuario.cep);
        formData.append("pais", this.usuario.pais);

        http
          .put("/api/v1/update-user/", formData, {
            headers: {
              Authorization: `Bearer ${VueCookies.get("accessToken")}`,
            },
          })
          .then(() => {
            Toast.fire({
              icon: "success",
              title: "Dados atualizados!",
            });
            this.getUser();
            window.scrollTo(0, 0);
          })
          .catch(() => {});
      } else {
        this.v$.$touch();
        window.scrollTo(0, 0);
      }
    },

    // Exclusão do Usuário logado
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
