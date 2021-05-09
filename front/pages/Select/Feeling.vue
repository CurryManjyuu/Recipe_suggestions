<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="orange accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/scene" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/start" x-large color="light-blue accent-1" block class="indigo--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <v-row class="center">
        <!-- カテゴリ別ボタン -->
        <v-col v-for="(post, i) in posts" :key="i" cols="12" md="4">
          <v-btn
            v-bind:color="post.color"
            class="white--text"
            x-large
            block
            @click="selectCategory(post.categoryId)"
          >
            <b>{{ post.categoryName }}</b>
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
      posts: [
        {
          "categoryName": "中華料理",
          "categoryId": "41",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "韓国料理",
          "categoryId": "42",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "イタリア料理",
          "categoryId": "43",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "フランス料理",
          "categoryId": "44",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "西洋料理",
          "categoryId": "25",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "エスニック料理・中南米",
          "categoryId": "46",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "沖縄料理",
          "categoryId": "47",
          "color": "light-blue darken-1"
        },
        {
          "categoryName": "日本各地の郷土料理",
          "categoryId": "48",
          "color": "light-blue darken-1"
        },
      ],
    };
  },
  methods: {
    // カテゴリ選択時に呼び出されるメソッド
    // カテゴリで抽出されたレシピ一覧ページへ遷移
    selectCategory: function(categoryId) {
      this.$router.push("/select/"+categoryId);
    }
  }
};
</script>
