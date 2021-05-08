<template>
  <div>
    <v-app-bar>
      <h1>今日のレシピ</h1>
      <v-btn
        to="/select/start"
        x-large
        color="pink accent-4"
        block
        class="white--text"
        ><b>何つくろう</b></v-btn
      >
      <Login style="position:absolute;top:5px;right:70px"></Login>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  components: {}
};
</script>
