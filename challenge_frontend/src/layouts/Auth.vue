<template>
  <div>
    <navbar />
    <main>
      <section class="relative w-full h-full py-40 min-h-screen">
        <div
          class="absolute top-0 w-full h-full bg-blueGray-800 bg-no-repeat bg-full"
          :style="`background-image: url('${registerBg2}');`"
        ></div>
        <router-view />
        <Footer absolute />
      </section>
    </main>
  </div>
</template>
<script>
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import Footer from "@/components/Footers/Footer.vue";

import registerBg2 from "@/assets/img/bg_color.png";

export default {
  data() {
    return {
      registerBg2,
    };
  },
  components: {
    Navbar,
    Footer,
  },
};
</script>
