<template>
  <v-app dark style="position:relative">
    <v-app-bar fixed app>
      <v-btn to="/">
        <v-toolbar-title v-text="title" />
      </v-btn>
      <v-spacer />
      <Login></Login>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-apps",
          title: "Welcome",
          to: "/"
        },
        {
          icon: "mdi-chart-bubble",
          title: "Inspire",
          to: "/inspire"
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Today's Recipe"
    };
  }
};
</script>
