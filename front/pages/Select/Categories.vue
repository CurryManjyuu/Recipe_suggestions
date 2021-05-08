<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/categories" x-large color="light-blue accent-1" block class="indigo--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
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
          "categoryName": "人気メニュー",
          "categoryId": "30",
          "color": "red accent-4"
        },
        {
          "categoryName": "定番の肉料理",
          "categoryId": "31",
          "color": "pink"
        },
        {
          "categoryName": "定番の魚料理",
          "categoryId": "32",
          "color": "pink"
        },
        {
          "categoryName": "卵料理",
          "categoryId": "33",
          "color": "amber accent-4"
        },
        {
          "categoryName": "ご飯もの",
          "categoryId": "14",
          "color": "grey lighten-1"
        },
        {
          "categoryName": "パスタ",
          "categoryId": "15",
          "color": "lime darken-3"
        },
        {
          "categoryName": "麺・粉物料理",
          "categoryId": "16",
          "color": "brown"
        },
        {
          "categoryName": "汁物・スープ",
          "categoryId": "17",
          "color": "teal lighten-2"
        },
        {
          "categoryName": "鍋料理",
          "categoryId": "23",
          "color": "purple darken-4"
        },
        {
          "categoryName": "サラダ",
          "categoryId": "18",
          "color": "green accent-4"
        },
        {
          "categoryName": "パン",
          "categoryId": "22",
          "color": "deep-orange darken-4"
        },
        {
          "categoryName": "お菓子",
          "categoryId": "21",
          "color": "purple accent-2"
        },
        {
          "categoryName": "肉",
          "categoryId": "10",
          "color": "pink darken-3"
        },
        {
          "categoryName": "魚",
          "categoryId": "11",
          "color": "blue"
        },
        {
          "categoryName": "野菜",
          "categoryId": "12",
          "color": "green darken-1"
        },
        {
          "categoryName": "果物",
          "categoryId": "34",
          "color": "orange accent-4"
        },
        {
          "categoryName": "ソース・ドレッシング",
          "categoryId": "19",
          "color": "teal accent-4"
        },
        {
          "categoryName": "飲みもの",
          "categoryId": "27",
          "color": "light-blue darken-2"
        },
        {
          "categoryName": "大豆・豆腐",
          "categoryId": "35",
          "color": "lime darken-4"
        },
        {
          "categoryName": "その他の食材",
          "categoryId": "13",
          "color": "red"
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
