<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large v-bind:color="color.category" block v-bind:class="categoryText"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large v-bind:color="color.method" block v-bind:class="methodText"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/feeling" x-large v-bind:color="color.feeling" block v-bind:class="feelingText"><b>地域から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <v-row class="center">
        <!-- 楽天のレシピページへのリンク付き画像 -->
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
      <v-row class="center">
        <v-col cols="12" md="4"></v-col>
        <v-col cols="12" md="4">
          <v-btn
            color="white"
            class="black--text more-btn"
            x-large
            block
            @click="getRecipe(1)"
            rounded
          >
            <b>もっと見る</b>
          </v-btn>
          <v-col cols="12" md="4"></v-col>
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
.more-btn {
  margin: 1em 0;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      categoryId: "",
      color: {
        category : "orange accent-4",
        method : "green accent-4",
        feeling : "light-blue accent-4"
      },
      categoryId : {
        category : ["30", "31", "32", "33", "14", "15", "16", "17", "23", "18", "22", "21", "10", "11", "12", "34", "19", "27", "35", "13"],
        method : ["20", "36", "37", "38", "39", "40", "24", "49", "50", "51", "52", "53", "54", "55", "26"],
        feeling : ["41", "42", "43", "44", "25", "46", "47", "48"]
      },
      categoryText: "white--text",
      methodText: "white--text",
      feelingText: "white--text"
    };
  },
  mounted () {
    // パラメータからカテゴリ群を取得してボタンの色を変更する。
    function inArray(value, array) {
      return [].indexOf.call(array, value);
    }
    if (inArray(this.$route.params.recipe, this.categoryId.category) >= 0) {
      this.color.category = "orange accent-1";
      this.categoryText = "deep-orange--text";
    } else if (inArray(this.$route.params.recipe, this.categoryId.method) >= 0) {
      this.color.method = "green accent-2";
      this.methodText = "teal--text"
    } else if (inArray(this.$route.params.recipe, this.categoryId.feeling) >= 0) {
      this.color.feeling = "light-blue accent-1";
      this.feelingText = "indigo--text";
    };
    // アクセス時に一度APIを叩いて4件取得する。
    axios
      .get("http://localhost:5000/recipe/large/"+this.$route.params.recipe+"/"+0)
      .then(response => (this.posts = response.data))
  },
  methods: {
    // 次へor前へボタンでAPPIを叩き、データを更新する。
    // 次へは0、前へは1を引数としてリクエストを投げる。
    getRecipe: function(index) {
      axios
        .get("http://localhost:5000/recipe/large/"+this.$route.params.recipe+"/"+index)
        .then(response => (this.posts.push(...response.data)));
    }
  }
};
</script>
