<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="orange accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/feeling" x-large color="light-blue accent-1" block class="indigo--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <!-- カテゴリ選択前 → カテゴリ一覧表示 -->
      <v-row class="center" v-if="select">
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
      <!-- カテゴリ選択後 → レシピ一覧表示 -->
      <v-row class="center" v-else>
        <!-- カテゴリ別ボタン -->
        <v-col v-for="(post, i) in posts" :key="i" cols="12" md="4">
          <!-- ボタンを押してアクションを実行 -->
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
      categoryId: "",
      select: false,
    };
  },
  methods: {
    // カテゴリ選択時に呼び出されるメソッド
    // データを新しく更新する
    selectCategory: function(id) {
      this.select = true;
      axios
        .get("http://localhost:5000/recipe/large/"+id)
        .then(response => (this.posts = response.data));
    }
  }
};
</script>
