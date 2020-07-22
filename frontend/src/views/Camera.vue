<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <h1>Vue Video Streaming Demonstration</h1>
        <img src="/video_feed" class="frame">
        <ul>
            <li v-for="post in posts" :key=post.id>
                {{ post }}
            </li>
        </ul>
        <form v-on:submit.prevent="submit">
            <input type="text" v-model="formData.text" value="default">
            <input type="submit" value="submit">
        </form>
        {{formData.text }} {{formData.text }}
    </div>
</template>

<style scoped>
    .frame {
        width: 50%;
        height: 50%;
    }
    
    li {
        list-style: none;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        name: 'Camera',
        data() {
            return {
                posts: [],
                host_url: 'http://127.0.0.1:8888/get_request',
                formData: {
                    'text': '',
                }
            }
        },
        mounted() {
            axios.get(this.host_url)
                .then(response => this.posts = response.data);
        },
        methods: {
            submit: async function () {

                axios.post(this.host_url, this.formData)
                    .then(response => {
                        this.posts = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    })
            }
        },
    }
</script>
