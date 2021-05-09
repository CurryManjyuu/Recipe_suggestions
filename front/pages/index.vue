<template>
  <v-app>
    <div>
      <h1>今日の飯</h1>
      <v-btn
        to="#"
        x-large
        color="pink accent-4"
        block
        class="white--text start-button"
        ><b>何つくろう？</b></v-btn
      >
    </div>
    <div class="large-category-btn-box">
    <v-container>
      <v-row class="center">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="orange accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/feeling" x-large color="light-blue accent-4" block class="white--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
    <v-row class="center">
      <!-- ランダムにレシピを表示 -->
      <v-col v-for="(post, i) in posts" :key="i" cols="12" md="3">
        <v-list flat>
          <v-list-item-group>
            <v-list-item v-bind:href="post.recipeUrl" target="_blank">
              <v-list-item-content>
                <v-img
                  v-bind:src="post.foodImageUrl"
                  aspect-ratio="1.7"
                  contain
                ></v-img>
                <v-list-item-title v-text="post.title" class="wrap-text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="4"></v-col>
      <v-col cols="12" md="4">
        <v-btn
          color="white"
          class="black--text"
          x-large
          block
          @click="getRandomRecipe()"
          rounded
          style="margin-bottom:4em;"
        >
          <b>もっと見る</b>
        </v-btn>
      </v-col>
      <v-col cols="12" md="4"></v-col>
    </v-row>
  </v-app>
</template>

<style scoped>
h1 {
  font-size: 4em;
  margin: 0;
  text-align: center;
}
.start-button {
  font-size: 1.75em;
  margin-bottom: 1em;
}
.large-category-btn-box {
  margin-bottom: 2em;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      categoryId: "",
    };
  },
  // アクセス時に一度APIを叩いて4件取得する。
  // 続いて同じAPIを叩くメソッドを呼び出す。
  mounted () {
    axios
      .get("http://localhost:5000/recipe/random")
      .then(response => {
          this.posts = response.data;
      });
  },
  methods: {
    getRandomRecipe: function() {
      axios
      .get("http://localhost:5000/recipe/random")
      .then(response => {
          this.posts.push(...response.data);
      });
    }
  }
};
</script>
