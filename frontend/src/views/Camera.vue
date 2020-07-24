<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <h1>Vue Video Streaming Demonstration</h1>
        <img src="/video_feed" class="frame">
        <form v-on:submit.prevent="submit" name="key_form">
            <input type="text" v-model="key" placeholder="key input">
            <input type="text" v-model="formData.text" placeholder="text">
            <input type="submit" value="submit">
        </form>
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
                request: [],
                formData: {
                    'text': '',
                    'key': '',
                },
                host_url: 'http://127.0.0.1:8888/get_request/',
                key: '',
                enabled_keys: ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight',
                    'a', 'd', 's', 'w',
                    'r', 'b', 'h', 'm',]
            }
        },
        watch: {
            key: function () {
                console.log(this.key);
                let host_url_param = this.host_url + this.key
                axios.get(host_url_param)
                    .then(response => this.request = response.data);
            }
        },
        mounted() {
            axios.get(this.host_url)
                .then(response => this.request = response.data);
            console.log('request get succeeded');

            let self = this;
            window.addEventListener('keydown', function (ev) {
                for (let i = 0; i < self.enabled_keys.length; i++) {
                    if (self.enabled_keys[i] === ev.key) {
                        self.key = ev.key
                    }
                }
            });
            window.addEventListener('keyup', function () {
                self.key = ''
            });
        },
        methods: {
            submit: function () {
                console.log('submit');
                axios.post(this.host_url, this.formData)
                    .then(response => {
                        this.request = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    })
            },
        },
    }
</script>
