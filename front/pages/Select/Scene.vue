<template>
  <div class="large-category-btn-box">
    <v-container>
      <v-row class="center" style="margin-bottom:1.5em;">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/categories"
            x-large
            color="orange accent-4"
            block
            class="white--text"
            ><b>材料から選ぶ</b></v-btn
          >
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/start"
            x-large
            color="green accent-2"
            block
            class="teal--text"
            ><b>シーンから選ぶ</b></v-btn
          >
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn
            rounded
            to="/select/feeling"
            x-large
            color="light-blue accent-4"
            block
            class="white--text"
            ><b>気分から選ぶ</b></v-btn
          >
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
          categoryName: "お弁当",
          categoryId: "20",
          color: "green lighten-1"
        },
        {
          categoryName: "簡単料理・時短",
          categoryId: "36",
          color: "green lighten-1"
        },
        {
          categoryName: "節約料理",
          categoryId: "37",
          color: "green lighten-1"
        },
        {
          categoryName: "今日の献立",
          categoryId: "38",
          color: "green lighten-1"
        },
        {
          categoryName: "健康料理",
          categoryId: "39",
          color: "green lighten-1"
        },
        {
          categoryName: "調理器具",
          categoryId: "40",
          color: "green lighten-1"
        },
        {
          categoryName: "行事・イベント",
          categoryId: "24",
          color: "green lighten-1"
        },
        {
          categoryName: "おせち料理",
          categoryId: "49",
          color: "green lighten-1"
        },
        {
          categoryName: "クリスマス",
          categoryId: "50",
          color: "green lighten-1"
        },
        {
          categoryName: "ひな祭り",
          categoryId: "51",
          color: "green lighten-1"
        },
        {
          categoryName: "春（3月～5月）",
          categoryId: "52",
          color: "green lighten-1"
        },
        {
          categoryName: "夏（6月～8月）",
          categoryId: "53",
          color: "green lighten-1"
        },
        {
          categoryName: "秋（9月～11月）",
          categoryId: "54",
          color: "green lighten-1"
        },
        {
          categoryName: "冬（12月～2月）",
          categoryId: "55",
          color: "green lighten-1"
        },
        {
          categoryName: "その他の目的・シーン",
          categoryId: "26",
          color: "green lighten-1"
        }
      ]
    };
  },
  methods: {
    // カテゴリ選択時に呼び出されるメソッド
    // カテゴリで抽出されたレシピ一覧ページへ遷移
    selectCategory: function(categoryId) {
      this.$router.push("/select/" + categoryId);
    }
  }
};
</script>
