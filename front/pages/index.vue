<template>
  <div>
    <h1>今日のレシピ</h1>
    <!-- <NuxtLink to="/fun">Home page</NuxtLink> -->
    <!-- <Logo></Logo> -->
    <!-- <VuetifyLogo></VuetifyLogo> -->
    <!-- <God></God> -->
    <!-- <Home></Home> -->
    <v-btn to="/select/start" x-large color="pink accent-4" block class="white--text"><b>何つくろう</b></v-btn>
    <!-- <Test></Test> -->
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import VuetifyLogo from "~/components/VuetifyLogo.vue";

export default {
  components: {
    Logo,
    VuetifyLogo,
  }
};
</script>
