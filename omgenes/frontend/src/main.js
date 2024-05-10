import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vue3GoogleLogin from 'vue3-google-login';
import LoadScript from "vue-plugin-load-script";

import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
    components,
    directives,
});

const app = createApp(App)

app.use(store)
.use(router)
.use(LoadScript)
.use(vuetify)
.use(vue3GoogleLogin, {clientId: "129850221361-koj4k3re7jjhr33i42ok2f3pj5f28mu2.apps.googleusercontent.com"})
.mount('#app')
