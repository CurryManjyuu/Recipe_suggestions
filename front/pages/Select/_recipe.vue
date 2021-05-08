<template>
  <div class="large-category-btn-box">
    <v-container>
      <h1>{{ $route.params.recipe }}</h1>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="orange accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/start" x-large color="light-blue accent-1" block class="indigo--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <v-row class="center">
        <!-- 楽天のレシピページへのリンク付き画像 -->
        <v-col v-for="(post, i) in posts" :key="i" cols="12" md="4">
          <v-item>
            <v-list-item-group>
              <v-list-item v-bind:href="post.recipeUrl" target="_blank">
                <v-list-item-content>
                  <v-img
                    v-bind:src="post.foodImageUrl"
                    aspect-ratio="1.7"
                    contain
                  ></v-img>
                  <v-list-item-title v-text="post.title"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-item>
        </v-col>
      </v-row>
      <v-row class="center">
        <v-col cols="12" md="3">
          <v-btn
            color="white"
            class="black--text"
            x-large
            block
            @click="getRecipe(0)"
          >
            <b>前へ</b>
          </v-btn>
        </v-col>
        <v-col cols="12" md="3"></v-col>
        <v-col cols="12" md="3"></v-col>
        <v-col cols="12" md="3">
          <v-btn
            color="white"
            class="black--text"
            x-large
            block
            @click="getRecipe(1)"
          >
            <b>次へ</b>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      categoryId: "",
    };
  },
  mounted () {
    axios
      .get("http://localhost:5000/recipe/large/"+this.$route.params.recipe+"/"+0)
      .then(response => (this.posts = response.data))
  },
  methods: {
    // 次へor前へボタンで呼び出され、データを更新する
    getRecipe: function(index) {
      axios
        .get("http://localhost:5000/recipe/large/"+this.$route.params.recipe+"/"+index)
        .then(response => (this.posts = response.data));
    }
  }
};
</script>
