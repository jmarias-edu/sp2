<template>
    <v-app>
      <v-app-bar :elevation="1" class="">
        <!-- <v-app-bar-title>OMGenes</v-app-bar-title> -->
        <template v-slot:prepend>
          <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
          <router-link to="/" style="height: 100%;"><img src="/appbarlogo.png" style="height: 100%;"/></router-link>
          <!-- <v-toolbar-title class="font-weight-bold ma-1">OMGenes</v-toolbar-title> -->
          <v-btn text to="/" class="ma-1">Home</v-btn>
          <v-btn text to="/genomebrowser" class="ma-1">Sample VCF</v-btn>
          <v-btn text to="/about" class="ma-1">About</v-btn>
          <v-btn text to="/workflow" class="ma-1">Workflow</v-btn>
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
      
      <v-navigation-drawer v-model="drawer" class="pa-4">
        <v-list-item to="/" link title="Home"></v-list-item>
        <v-list-item to="/genomebrowser" link title="Sample VCF"></v-list-item>
        
        <v-divider></v-divider>
        <div v-if="isEmpty(user)"></div>
        <div v-else>
          <v-toolbar-title class="font-weight-bold">VCF Reads</v-toolbar-title>
          <v-list-item to="/newproj" link><h3>Create New Read</h3></v-list-item>
          
          <v-list-item v-for="read in reads" 
          :key="read.id" 
          :to="{name: 'variantreads', params: {id: read.id}}"
          link>
            <v-list-item-content>
              <v-list-item-title>{{ read.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-toolbar-title class="font-weight-bold">Variant Calls</v-toolbar-title>
          <v-list-item to="/newcall" link><h3>Create New Call</h3></v-list-item>

          <v-list-item v-for="call in calls" 
          :key="call.id" 
          :to="{name: 'variantcalls', params: {id: call.id}}"
          link>
            <v-list-item-content>
              <v-list-item-title>{{ call.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          


        </div>
      </v-navigation-drawer>

      

      <v-main>
        <router-view :key="$route.fullPath"/>      
        
      </v-main>


    <!--  -->
    <v-overlay v-model="isLoading" class="d-flex justify-center align-center flex-column" persistent absolute>
      <v-progress-circular indeterminate color="primary" :size="100" :width="10"></v-progress-circular>
      <!-- <v-text>Loading...</v-text> -->
    </v-overlay>

    <v-snackbar v-model="snackbar.show" :color="snackbar.color" top right timeout="3000">
      {{ snackbar.message }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbar.show = false">Close</v-btn>
      </template>
    </v-snackbar>

  </v-app>

</template>

<script>
  import googleAPI from "./api/auth"
  import fileHandler from "@/api/file"
  import callHandler from "@/api/call"
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
        snackbar: {
          show: false,
          message: '',
          color: 'info',
        }
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
        this.showToast("Successfully logged out!")
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
        }).then(response =>{
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
      fetchCalls(){
        callHandler.fetchCalls().then(
          response => {
            console.log(response.data)
            this.calls = response.data.calls
          }
        )
      },
      showToast(message, color = 'info') {
        this.snackbar.message = message;
        this.snackbar.color = color;
        this.snackbar.show = true;
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
          this.fetchCalls();
          this.showToast("Data fetched!");
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