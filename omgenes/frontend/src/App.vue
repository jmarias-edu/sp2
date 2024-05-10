<template>
    <v-app>
    <v-navigation-drawer>
      <v-list-item title="OMGenes LMAO"></v-list-item>
      <v-divider></v-divider>
      <router-link to="/"><v-list-item title="Home"></v-list-item></router-link>
      <router-link to="/about"><v-list-item link title="About"></v-list-item></router-link>
    </v-navigation-drawer>
    <v-app-bar :elevation="5">
      <v-app-bar-title>OMGenes</v-app-bar-title>
      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <GoogleLogin :callback="callback"/>
      </template>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>

</template>


<script setup> 
  import { onMounted } from 'vue'
  import {loadScript} from "vue-plugin-load-script";
  import googleAPI from "./api/auth"
  const callback = (response) => {
    console.log("Handle the response", response);
    console.log(googleAPI.googleCallback(response));

  }
  onMounted(() => {
    console.log(`the component is now mounted.`)
  })
</script>