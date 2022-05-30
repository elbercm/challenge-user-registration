<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-6/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-6">
            <div class="text-center mb-3">
              <h6 class="text-blueGray-500 text-sm font-bold">
                PÁGINA DE CADASTRO
              </h6>
            </div>

            <hr class="mt-6 border-b-1 border-blueGray-300" />
          </div>
          <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
            <form @submit.prevent="cadUserSubmit">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="name"
                >
                  Nome
                  <small
                    v-if="submitted && v$.formCadUser.name.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Nome é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="name"
                  v-model="formCadUser.name"
                />
              </div>
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="email"
                >
                  Email
                  <small
                    v-if="submitted && v$.formCadUser.email.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    E-mail inválido*
                  </small>
                </label>
                <input
                  type="email"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="email"
                  v-model="formCadUser.email"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="CPF"
                >
                  cpf
                  <small
                    v-if="submitted && v$.formCadUser.cpf.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    CPF é requerido*
                  </small>
                  <small
                    v-if="submitted && v$.formCadUser.cpf.cpfValid.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Número do CPF inválido*
                  </small>
                </label>
                <input
                  v-maska="'###.###.###-##'"
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="CPF"
                  v-model="formCadUser.cpf"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="PIS"
                >
                  PIS
                  <small
                    v-if="submitted && v$.formCadUser.pis.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    PIS é requerido*
                  </small>
                  <small
                    v-if="submitted && v$.formCadUser.pis.pisValid.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Número do PIS inválido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="PIS"
                  v-maska="'###.#####.##-#'"
                  v-model="formCadUser.pis"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="endereco"
                >
                  Endereço
                  <small
                    v-if="
                      submitted && v$.formCadUser.endereco.required.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Endereço é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="endereco"
                  v-model="formCadUser.endereco"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="numero"
                >
                  Número
                  <small
                    v-if="submitted && v$.formCadUser.numero.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Número é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="numero"
                  v-model="formCadUser.numero"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="estado"
                >
                  Estado
                  <small
                    v-if="submitted && v$.formCadUser.estado.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Estado é requerido*
                  </small>
                </label>
                <select
                  v-model="formCadUser.estado"
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

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="complemento"
                >
                  Complemento
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="complemento"
                  v-model="formCadUser.complemento"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  id="municipio"
                >
                  Município
                  <small
                    v-if="
                      submitted && v$.formCadUser.municipio.required.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Município é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="municipio"
                  v-model="formCadUser.municipio"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="bairro"
                >
                  Bairro
                  <small
                    v-if="submitted && v$.formCadUser.bairro.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Bairro é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="bairro"
                  v-model="formCadUser.bairro"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="CEP"
                >
                  CEP
                  <small
                    v-if="submitted && v$.formCadUser.cep.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    CEP é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="CEP"
                  v-maska="'#####-###'"
                  v-model="formCadUser.cep"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="pais"
                >
                  País
                  <small
                    v-if="submitted && v$.formCadUser.pais.required.$invalid"
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    País é requerido*
                  </small>
                </label>
                <input
                  type="text"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="pais"
                  v-model="formCadUser.pais"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="password"
                >
                  Password
                  <small
                    v-if="
                      submitted && v$.formCadUser.password.required.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Senha é requerido*
                  </small>
                  <small
                    v-if="
                      submitted && v$.formCadUser.password.minLength.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    A senha deve ter pelo menos 8 caracteres* </small
                  ><br />
                  <small
                    v-if="
                      submitted &&
                      v$.formCadUser.password.passwordRegexValidate.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    A senha deve conter pelo menos um nº, uma letra maiúscula e
                    uma letra minúscula!*
                  </small>

                  <!-- <div
                    class="input-errors"
                    v-for="error of v$.formCadUser.$errors"
                    :key="error.$uid"
                  >
                    <div class="error-msg">
                      {{ error }}
                    </div>
                  </div> -->
                </label>
                <input
                  type="password"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="password"
                  name="password"
                  v-model="formCadUser.password"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  for="re_password"
                >
                  Confirmação de senha:
                  <small
                    v-if="
                      submitted && v$.formCadUser.re_password.required.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    Necessário confirmação de senha*
                  </small>

                  <small
                    v-if="
                      submitted && v$.formCadUser.re_password.sameAs.$invalid
                    "
                    class="font-bold leading-normal mt-0 mb-4 text-red-500"
                  >
                    As senhas devem ser iguais*
                  </small>
                </label>
                <input
                  type="password"
                  class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  id="re_password"
                  v-model="formCadUser.re_password"
                />
              </div>

              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                >
                  criar conta
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {
  required,
  email,
  minLength,
  helpers,
  sameAs,
} from "@vuelidate/validators";
import { maska } from "maska";
import { pisValid, cpfValid, passwordRegex } from "@/plugins/utils";
import useVuelidate from "@vuelidate/core";
import { http } from "@/axios/axios.js";
import Swal from "sweetalert2";
const passwordRegexValidate = helpers.regex(passwordRegex);

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
  name: "Register",
  directives: { maska },
  setup() {
    return { v$: useVuelidate() };
  },
  data() {
    return {
      formCadUser: {
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
        password: "",
        re_password: "",
      },
      submitted: false,
    };
  },
  validations() {
    return {
      formCadUser: {
        name: {
          required,
        },
        email: { required, email },
        cpf: { required, cpfValid },
        pis: { required, pisValid },
        endereco: { required },
        numero: { required },
        estado: { required },
        municipio: { required },
        bairro: { required },
        cep: { required },
        pais: { required },
        password: { required, passwordRegexValidate, minLength: minLength(8) },
        re_password: { required, sameAs: sameAs(this.formCadUser.password) },
      },
    };
  },
  methods: {
    cadUserSubmit() {
      this.submitted = true;

      if (!this.v$.$invalid) {
        const formData = new FormData();
        formData.append("name", this.formCadUser.name);
        formData.append("email", this.formCadUser.email);
        formData.append("cpf", this.formCadUser.cpf);
        formData.append("pis", this.formCadUser.pis);
        formData.append("endereco", this.formCadUser.endereco);
        formData.append("numero", this.formCadUser.numero);
        formData.append("estado", this.formCadUser.estado);
        formData.append("complemento", this.formCadUser.complemento);
        formData.append("cidade", this.formCadUser.municipio);
        formData.append("bairro", this.formCadUser.bairro);
        formData.append("cep", this.formCadUser.cep);
        formData.append("pais", this.formCadUser.pais);
        formData.append("password", this.formCadUser.password);
        formData.append("re_password", this.formCadUser.re_password);
        http
          .post("/api/v1/register-user/", formData)
          .then(() => {
            Swal.fire({
              title: "Cadastro Realizado!",
              icon: "success",
            }).then((result) => {
              result === "success";
              this.$router.push("/auth/login");
            });
          })
          .catch((e) => {
            Toast.fire({
              icon: "error",
              title: e.response.data.error.toString().split("'")[3],
            });
          });
      } else {
        this.v$.$touch();
        window.scrollTo(0, 0);
      }
    },
  },
};
</script>
