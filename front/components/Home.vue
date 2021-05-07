<template>
  <div>
    <p>Home page</p>
    <p>外山</p>
    <button @click="hantei = !hantei">sleep</button>
    <p v-if="hantei">{{ toyamabaka }}</p>
    <p v-else>{{ toyama }}</p>
    <button @click="apiTest">apiTest</button>
    <p>{{ posts }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hello: "hello2",
      toyama: "toyamaは天才",
      toyamabaka: "toyamaはバカ",
      hantei: true,
      posts: []
    };
  },
  methods: {
    apiTest: function() {
      this.$axios.$get("http://localhost:5000/hoge").then(response => {
        console.log("response", response);
        this.posts = response;
      });
    },
    mounted() {}
    //https://date.nager.at/api/v2/publicholidays/2017/AT
    //https://pokeapi.co/api/v2/ability/7/")
  }
};
</script>
