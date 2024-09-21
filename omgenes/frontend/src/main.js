import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vue3GoogleLogin from 'vue3-google-login';
import LoadScript from "vue-plugin-load-script";
import VueCookies from 'vue-cookies'


import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
    components,
    directives,
    deafultTheme: "light",
    themes: {
        light: {
          primary: '#1976D2',
          secondary: '#424242',
          accent: '#82B1FF',
          // You can add or override colors in the default theme
        },
    }
});

const app = createApp(App)

app.use(store)
.use(router)
.use(LoadScript)
.use(vuetify)
.use(vue3GoogleLogin, {clientId: "129850221361-koj4k3re7jjhr33i42ok2f3pj5f28mu2.apps.googleusercontent.com"})
.use(VueCookies)
.mount('#app')
