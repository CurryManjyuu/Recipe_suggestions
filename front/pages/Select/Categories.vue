<template>
  <div class="large-category-btn-box">
    <NuxtLink to="/">ホームへ戻る</NuxtLink>
    <v-container>
      <!-- カテゴリ選択前 → カテゴリ一覧表示 -->
      <v-row class="center" v-if="select">
        <!-- （楽天ページへの）リンク付き画像 -->
        <v-col
          v-for="(post, i) in posts"
          :key="i"
          cols="12"
          md="4"
        >
          <v-item>
            <v-list-item-group>
              <v-list-item to="/">
                <v-list-item-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-img src="https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg?thum=55" aspect-ratio="1.7" contain></v-img>
                  <v-list-item-title v-text="post.name"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-item>
        </v-col>
      </v-row>
      <!-- カテゴリ選択後 → レシピ一覧表示 -->
      <v-row class="center" v-else>
        <!-- カテゴリ別ボタン -->
        <v-col
          v-for="(post, i) in posts"
          :key="i"
          cols="12"
          md="4"
        >
          <!-- ボタンを押してアクションを実行 -->
          <v-btn
            color="green accent-4"
            class="white--text"
            x-large
            block
            @click="selectCategory(post.id)"
          >
            <b>{{ post.id }}</b>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
     posts: [],
     categoryId: "",
     select: false
    }
  },
  mounted () {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then((response) => this.posts = response.data)
  },
  methods: {
    // カテゴリ選択時に呼び出されるメソッド
    // データを新しく更新する
    selectCategory: function(id) {
      this.select = true
      axios.get('https://randomuser.me/api/', {
        params: {
          results: id
        }})
      .then((response) => this.posts = response.data.results)
    }
  }
}
</script>