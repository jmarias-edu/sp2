<template>
    <v-app>
    <v-navigation-drawer v-model="drawer">
      <v-toolbar-title class="font-weight-bold">OMGenes Navigation</v-toolbar-title>
      <v-divider></v-divider>
      <v-list-item to="/" link title="Home"></v-list-item>
      <v-list-item to="/about" link title="Genome Browser"></v-list-item>
      
      <v-divider></v-divider>
      <div v-if="isEmpty(user)"></div>
      <div v-else>
        <v-toolbar-title class="font-weight-bold">Your Projects</v-toolbar-title>
        <v-list-item to="/newproj" link title="Create New Project"></v-list-item>
      </div>
    </v-navigation-drawer>
    <v-app-bar :elevation="1">
      <v-app-bar-title>OMGenes</v-app-bar-title>
      <template v-slot:prepend><v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon></template>
      <template v-slot:append>
        <div v-if="isEmpty(user)">
          <GoogleLogin :callback="callback"/>
        </div>
        <div v-else>
          <a>Welcome {{user["fname"]}}! </a>
          <v-app-bar-nav-icon icon @click="logout"><v-icon>mdi-logout</v-icon></v-app-bar-nav-icon>
        </div>
      </template>
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
  import { decodeCredential } from 'vue3-google-login'

  export default {
    data(){
      return {
        user: {},
        drawer: true
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
        // console.log(response.credential);
        const userData = decodeCredential(response.credential);
        console.log("Handle the user data", userData);
        const userToken = response.credential
        
        googleAPI.googleCallback(userToken).then(response => {
          console.log(response);
          console.log("Token ".concat(response.data["token"]));
          VueCookies.set("authtoken", "Token ".concat(response.data["token"]), "1d");
          console.log(VueCookies.get("csrftoken"))
          const fetcheduser = {"email": response.data["email"], "fname": response.data["fname"]};
          this.user = fetcheduser;
          this.$router.push({path: "/"})
        });
      },
      toggleDrawer() {
        this.drawer = !this.drawer;
      }
    },
    mounted(){
      if(VueCookies.get("authtoken")){
        
        googleAPI.fetchUser().then(response => {
          this.user = {"email": response.data["email"], "fname":response.data["fname"]}
        })
      }
    }
  }

  

</script>