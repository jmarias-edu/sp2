<template>
    <v-app>

      <v-navigation-drawer v-model="drawer" class="pa-4">
        <v-toolbar-title class="font-weight-bold">OMGenes</v-toolbar-title>
        <v-divider></v-divider>
        <v-list-item to="/" link title="Home"></v-list-item>
        <v-list-item to="/genomebrowser" link title="Sample VCF"></v-list-item>
        
        <v-divider></v-divider>
        <div v-if="isEmpty(user)"></div>
        <div v-else>
          <v-toolbar-title class="font-weight-bold">VCF Reads</v-toolbar-title>
          <v-list-item to="/newproj" link title="Create New Read"></v-list-item>
          
          <v-list-item v-for="read in reads" 
          :key="read.id" 
          :to="{name: 'variantreads', params: {id: read.id}}"
          link>
            <v-list-item-content>
              <v-list-item-title>{{ read.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-toolbar-title class="font-weight-bold">Variant Calls</v-toolbar-title>
          <v-list-item to="/newcall" link title="Create New Call"></v-list-item>
          


        </div>
      </v-navigation-drawer>

      <v-app-bar :elevation="1">
        <!-- <v-app-bar-title>OMGenes</v-app-bar-title> -->
        <template v-slot:prepend>
          <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
          <!-- <v-btn @click="fetchReads">Test Fetch</v-btn> -->
        </template>
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
        <router-view :key="$route.fullPath"/>      
        
      </v-main>


    <!--  -->
    <v-overlay v-model="isLoading" class="d-flex justify-center align-center flex-column" persistent absolute>
      <v-progress-circular indeterminate color="primary" :size="100" :width="10"></v-progress-circular>
      <!-- <v-text>Loading...</v-text> -->
    </v-overlay>
  </v-app>

</template>

<script>
  import googleAPI from "./api/auth"
  import fileHandler from "@/api/file"
  import VueCookies from "vue-cookies"
  import { onMounted, mounted } from 'vue'
  import { decodeCredential } from 'vue3-google-login'

  export default {
    data(){
      return {
        user: {},
        drawer: true,
        reads: [],
        calls: [],
        isLoading: false,
      }
    },
    methods: {
      isEmpty(obj) {
        return Object.keys(obj).length === 0
      },
      logout(){
        this.startLoading();
        setTimeout(()=>{
          console.log("Logging out");
        }, 2000)
        this.user = {}
        this.reads = []
        this.calls = []
        VueCookies.remove("authtoken");
        VueCookies.remove("csrftoken");
        this.$router.push({path: "/"});
        this.stopLoading();
      },
      callback(response) {
        this.startLoading();
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
          this.$router.push({path: "/"});
        }).then(response => {
          this.$forceUpdate();
          this.$router.go(0);
          this.stopLoading();
        })
      },
      toggleDrawer() {
        this.drawer = !this.drawer;
      },
      fetchReads(){
        fileHandler.fetchReads().then(
          response => {
            console.log(response.data)
            this.reads = response.data.reads
          }
        )
      },
      startLoading(){
        this.isLoading = true;
      },
      stopLoading(){
        this.isLoading = false;
      },
      // removeRead(readID){
      //   this.reads = this.reads.filter(obj => obj.id !==readID);
      //   console.log(this.reads)
      //   this.$forceUpdate();
      // },

    },
    // provide(){
    //   return {
    //     removeID: this.removeRead
    //   }
    // },
    mounted(){
      if(VueCookies.get("authtoken")){
        googleAPI.fetchUser().then(response => {
          this.user = {"email": response.data["email"], "fname":response.data["fname"]};
          this.fetchReads();
        })
      }
    }
  }

  

</script>

<style>
  .v-app {
    position: relative;
  }
</style>