<template>
  <v-app>
    <div>
      <h1>今日の飯</h1>
      <v-btn
        to="/select/start"
        x-large
        color="pink accent-4"
        block
        class="white--text start-button"
        ><b>何つくろう</b></v-btn
      >
    </div>
  </v-app>
</template>

<style scoped>
h1 {
  font-size: 8.5em;
  margin: 0.5em auto;
  text-align: center;
}
.start-button {
  font-size: 1.75em;
}
</style>

<script>
export default {
  components: {}
};
</script>
