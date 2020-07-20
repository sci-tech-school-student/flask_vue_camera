<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Vue Video Streaming Demonstration</h1>
    <img src="/video_feed" class="frame">
  </div>
</template>

<style scoped>
.frame {
  width: 100%;
  height: 100%;
}
</style>

<script>
  export default {
    name: 'Camera',
  }
</script>
