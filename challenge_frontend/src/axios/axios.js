import axios from "axios";

const http = axios.create({
  baseURL: "http://191.252.109.31:8443/",
  timeout: 1000,
});

export { http };
