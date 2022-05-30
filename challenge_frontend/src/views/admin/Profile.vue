<template>
  <div class="flex content-center items-center justify-center h-full">
    <div class="lg:w-8/12 px-4">
      <CardProfile />
    </div>
  </div>
</template>
<script>
import CardProfile from "@/components/Cards/CardProfile.vue";

export default {
  components: {
    CardProfile,
  },
};
</script>
