<template>
  <div class="large-category-btn-box">
    <NuxtLink to="/">ホームへ戻る</NuxtLink>
    <v-container>
      <v-row class="center">
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn to="/select/categories" x-large color="light-blue accent-4" block class="white--text"><b>材料から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn to="/select/method" x-large color="green accent-1" block class="black--text"><b>作り方から選ぶ</b></v-btn>
        </v-col>
        <v-col cols="12" sm="12" md="4" lg="4">
          <v-btn to="/select/feeling" x-large color="orange accent-4" block class="white--text"><b>気分から選ぶ</b></v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          v-for="(post, i) in posts"
          :key="i"
          cols="12"
          md="4"
        >
          <v-item>
            <v-list-item-group>
              <v-list-item>
                <v-list-item-icon>
                  <v-icon v-text="post.name.title"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="post.name.last"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-item>
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
    }
  },
  mounted () {
    axios.get('https://randomuser.me/api/', {
        params: {
          results: '30'
        }})
      .then((response) => this.posts = response.data.results)
  }
}
</script>