<template>
  <div class="">
    <div class="row">
      <div class="col-md-5">
        <h4>Welcome to Our Gallery Photos</h4>
        <br>
        <p v-bind:key="post.id" v-for="post in posts['results']">
          <b>{{ post.title }}</b>
          <br>
          {{ post.body }}
        </p>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ListPosts",
  components: {

  },
  data() {
    return {
      posts : [],
    }
  },
  methods: {
    "getPosts"() {
      axios.get("http://localhost:8000/posts/?page=2").then(res => (this.posts = res.data))
      .catch(err => console.log(err));
    },
  },
  created() {
    this.getPosts();
  }
}
</script>

<style scoped>

</style>