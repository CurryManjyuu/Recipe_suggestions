<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/categories"
            x-large
            :color="color0"
            block
            class="white--text"
            ><b>材料から選ぶ</b></v-btn
          >
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/scene"
            x-large
            :color="color1"
            block
            class="white--text"
            ><b>シーンから選ぶ</b></v-btn
          >
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/feeling"
            x-large
            :color="color2"
            block
            class="white--text"
            ><b>気分から選ぶ</b></v-btn
          >
        </v-col>
      </v-row>
      <v-row class="center">
        <!-- 楽天のレシピページへのリンク付き画像 -->
        <v-col
          v-for="(post, i) in posts"
          :key="i"
          cols="12"
          md="3"
          style="margin:2em 0;"
        >
          <v-list flat>
            <v-list-item-group>
              <v-list-item v-bind:href="post.recipeUrl" target="_blank">
                <v-list-item-content>
                  <v-img
                    v-bind:src="post.foodImageUrl"
                    aspect-ratio="1.7"
                    contain
                  ></v-img>
                  <v-list-item-title
                    v-text="post.title"
                    class="wrap-text"
                  ></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
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

<style scoped>
.wrap-text {
  word-break: break-all;
  white-space: normal;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      categoryId: "",
      color0: "",
      color1: "",
      color2: ""
    };
  },
  // アクセス時に一度APIを叩いて4件取得する。
  mounted() {
    axios
      .get(
        "http://localhost:5000/recipe/large/" +
          this.$route.params.recipe +
          "/" +
          0
      )
      .then(response => (this.posts = response.data));
    var params = this.$route.params.recipe;
    if (
      params == "30" ||
      params == "31" ||
      params == "32" ||
      params == "33" ||
      params == "14" ||
      params == "15" ||
      params == "16" ||
      params == "17" ||
      params == "23" ||
      params == "18" ||
      params == "22" ||
      params == "21" ||
      params == "10" ||
      params == "11" ||
      params == "12" ||
      params == "34" ||
      params == "19" ||
      params == "27" ||
      params == "35" ||
      params == "13"
    ) {
      this.color0 = "orange accent-1";
      this.color1 = "green accent-4";
      this.color2 = "light-blue accent-4";
    }
    if (
      params == "41" ||
      params == "42" ||
      params == "43" ||
      params == "44" ||
      params == "25" ||
      params == "46" ||
      params == "47" ||
      params == "48"
    ) {
      this.color0 = "orange accent-4";
      this.color1 = "green accent-4";
      this.color2 = "light-blue accent-1";
    }
    if (
      params == "20" ||
      params == "36" ||
      params == "37" ||
      params == "38" ||
      params == "38" ||
      params == "40" ||
      params == "24" ||
      params == "49" ||
      params == "50" ||
      params == "51" ||
      params == "52" ||
      params == "53" ||
      params == "54" ||
      params == "55" ||
      params == "26"
    ) {
      this.color0 = "orange accent-4";
      this.color1 = "green accent-1";
      this.color2 = "light-blue accent-4";
    }
  },
  methods: {
    // 次へor前へボタンでAPPIを叩き、データを更新する。
    // 次へは0、前へは1を引数としてリクエストを投げる。
    getRecipe: function(index) {
      axios
        .get(
          "http://localhost:5000/recipe/large/" +
            this.$route.params.recipe +
            "/" +
            index
        )
        .then(response => (this.posts = response.data));
    }
  }
};
</script>
