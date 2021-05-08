<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/start" x-large color="orange accent-1" block class="deep-orange--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/method" x-large color="green accent-4" block class="white--text"><b>シーンから選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn rounded to="/select/feeling" x-large color="light-blue accent-4" block class="white--text"><b>気分から選ぶ</b></v-btn>
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
          "categoryName": "人気メニュー",
          "categoryId": "30",
          "color": "orange darken-1"
        },
        {
          "categoryName": "定番の肉料理",
          "categoryId": "31",
          "color": "orange darken-1"
        },
        {
          "categoryName": "定番の魚料理",
          "categoryId": "32",
          "color": "orange darken-1"
        },
        {
          "categoryName": "卵料理",
          "categoryId": "33",
          "color": "orange darken-1"
        },
        {
          "categoryName": "ご飯もの",
          "categoryId": "14",
          "color": "orange darken-1"
        },
        {
          "categoryName": "パスタ",
          "categoryId": "15",
          "color": "orange darken-1"
        },
        {
          "categoryName": "麺・粉物料理",
          "categoryId": "16",
          "color": "orange darken-1"
        },
        {
          "categoryName": "汁物・スープ",
          "categoryId": "17",
          "color": "orange darken-1"
        },
        {
          "categoryName": "鍋料理",
          "categoryId": "23",
          "color": "orange darken-1"
        },
        {
          "categoryName": "サラダ",
          "categoryId": "18",
          "color": "orange darken-1"
        },
        {
          "categoryName": "パン",
          "categoryId": "22",
          "color": "orange darken-1"
        },
        {
          "categoryName": "お菓子",
          "categoryId": "21",
          "color": "orange darken-1"
        },
        {
          "categoryName": "肉",
          "categoryId": "10",
          "color": "orange darken-1"
        },
        {
          "categoryName": "魚",
          "categoryId": "11",
          "color": "orange darken-1"
        },
        {
          "categoryName": "野菜",
          "categoryId": "12",
          "color": "orange darken-1"
        },
        {
          "categoryName": "果物",
          "categoryId": "34",
          "color": "orange darken-1"
        },
        {
          "categoryName": "ソース・ドレッシング",
          "categoryId": "19",
          "color": "orange darken-1"
        },
        {
          "categoryName": "飲みもの",
          "categoryId": "27",
          "color": "orange darken-1"
        },
        {
          "categoryName": "大豆・豆腐",
          "categoryId": "35",
          "color": "orange darken-1"
        },
        {
          "categoryName": "その他の食材",
          "categoryId": "13",
          "color": "orange darken-1"
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
