<template>
  <v-app>
    <div>
      <h1>今日のレシピ</h1>
      <v-btn
        to="/select/start"
        x-large
        color="pink accent-4"
        block
        class="white--text"
        ><b>何つくろう</b></v-btn
      >
    </div>
  </v-app>
</template>

<style scoped>
h1 {
  font-size: 8em;
  margin: 0.5em auto;
  text-align: center;
}
</style>

<script>
export default {
  components: {}
};
</script>
