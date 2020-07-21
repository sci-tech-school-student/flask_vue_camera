<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <h1>Vue Video Streaming Demonstration</h1>
        <img src="/video_feed" class="frame">
        <ul>
            <li v-for="post in posts" :key=post.id>
                {{ post.id }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .frame {
        width: 50%;
        height: 50%;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        name: 'Camera',
        data() {
            return {
                posts: [],
            }
        },
        mounted() {
            axios.get('https://jsonplaceholder.typicode.com/posts')
                .then(response => this.posts = response.data);
        },
    }
</script>
