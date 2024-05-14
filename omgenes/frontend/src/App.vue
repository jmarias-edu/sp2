<template>
    <v-app>
    <v-navigation-drawer>
      <v-list-item title="OMGenes"></v-list-item>
      <v-divider></v-divider>
      <router-link to="/"><v-list-item title="Home"></v-list-item></router-link>
      <router-link to="/about"><v-list-item link title="About"></v-list-item></router-link>
    </v-navigation-drawer>
    <v-app-bar :elevation="5">
      <v-app-bar-title>OMGenes</v-app-bar-title>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <GoogleLogin :callback="callback" v-if="isEmpty(user)"/>
        <div v-else>
          <a>Welcome {{user["email"]}}!</a>
          <a @click="logout">Logout</a>
        </div>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>

</template>

<script>
  import googleAPI from "./api/auth"
  import VueCookies from "vue-cookies"
  import { onMounted, mounted } from 'vue'
  export default {
    data(){
      return {
        user: {}
      }
    },
    methods: {
      isEmpty(obj) {
        return Object.keys(obj).length === 0
      },
      logout(){
        this.user = {}
        VueCookies.remove("authtoken");
        VueCookies.remove("csrftoken");
        this.$router.push({path: "/"})
      },
      callback(response) {
        console.log("Handle the response", response);
        googleAPI.googleCallback(response.credential).then(response => {
          console.log(response);
          console.log("Token ".concat(response.data["token"]));
          VueCookies.set("authtoken", "Token ".concat(response.data["token"]), "1d");
          console.log(VueCookies.get("csrftoken"))
          const fetcheduser = {"email": response.data["email"]};
          this.user = fetcheduser;
          this.$router.push({path: "/"})
        });
      }
    },
    mounted(){
      if(VueCookies.get("authtoken")){
        this.user = {"email": "name"}
        googleAPI.fetchUser().then(response => {
          console.log(response);
        })
      }
    }
  }

  

</script>