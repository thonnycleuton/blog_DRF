<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <ListPosts msg="Welcome to Our Wedding Gallery"/>
  </div>
</template>

<script>
// @ is an alias to /src

import ListPosts from "@/components/ListPosts";

export default {
  name: 'Home',
  components: {
    ListPosts
  }
}
</script>
