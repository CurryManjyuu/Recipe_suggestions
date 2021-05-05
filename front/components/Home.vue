<template>
  <div>
    <p>Home page</p>
    <p>外山</p>
    <button @click="hantei = !hantei">sleep</button>
    <p v-if="hantei">{{ toyamabaka }}</p>
    <p v-else>{{ toyama }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hello: "hello2",
      toyama: "toyamaは天才",
      toyamabaka: "toyamaはバカ",
      hantei: true
    };
  },
  methods: {
    apiTest: function() {
      
    }
  }
};
</script>
