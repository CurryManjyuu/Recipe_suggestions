<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="light-blue accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-1" block class="teal--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/feeling" x-large color="orange accent-4" block class="white--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <!-- カテゴリ選択前 → カテゴリ一覧表示 -->
      <v-row class="center" v-if="select">
        <!-- 楽天のレシピページへのリンク付き画像 -->
        <v-col v-for="(post, i) in posts" :key="i" cols="12" md="4">
          <v-item>
            <v-list-item-group>
              <v-list-item v-bind:href="post.recipeUrl" target="_blank">
                <v-list-item-icon> </v-list-item-icon>
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
        "categoryName": "お弁当",
        "categoryId": "20",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/20/"
      },
      {
        "categoryName": "簡単料理・時短",
        "categoryId": "36",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/36/"
      },
      {
        "categoryName": "節約料理",
        "categoryId": "37",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/37/"
      },
      {
        "categoryName": "今日の献立",
        "categoryId": "38",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/38/"
      },
      {
        "categoryName": "健康料理",
        "categoryId": "39",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/39/"
      },
      {
        "categoryName": "調理器具",
        "categoryId": "40",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/40/"
      },
      {
        "categoryName": "行事・イベント",
        "categoryId": "24",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/24/"
      },
      {
        "categoryName": "おせち料理",
        "categoryId": "49",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/49/"
      },
      {
        "categoryName": "クリスマス",
        "categoryId": "50",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/50/"
      },
      {
        "categoryName": "ひな祭り",
        "categoryId": "51",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/51/"
      },
      {
        "categoryName": "春（3月～5月）",
        "categoryId": "52",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/52/"
      },
      {
        "categoryName": "夏（6月～8月）",
        "categoryId": "53",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/53/"
      },
      {
        "categoryName": "秋（9月～11月）",
        "categoryId": "54",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/54/"
      },
      {
        "categoryName": "冬（12月～2月）",
        "categoryId": "55",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/55/"
      },
      {
        "categoryName": "その他の目的・シーン",
        "categoryId": "26",
        "categoryUrl": "https://recipe.rakuten.co.jp/category/26/"
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
        .get("http://localhost:5000/recipe/large", {
          params: {
            category_id: id
          }
        })
        .then(response => (this.posts = response.data));
    }
  }
};
</script>