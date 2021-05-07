<template>
 <div class="page">
   <p>{{ posts }}</p>
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
   axios.get('https://jsonplaceholder.typicode.com/posts')
     .then((response) => this.posts = response)
 }
}
</script>
