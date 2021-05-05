<template>
  <div>
    <h1>Hello world!</h1>
    <NuxtLink to="/fun">Home page</NuxtLink>
    <Logo></Logo>
    <VuetifyLogo></VuetifyLogo>
    <God></God>
    <Home></Home>
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import VuetifyLogo from "~/components/VuetifyLogo.vue";

export default {
  components: {
    Logo,
    VuetifyLogo
  }
};
</script>
