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
const callback = (response) => {
  console.log("Handle the response", response)
}
</script>

// <style lang="scss">
// #app {
//   font-family: Avenir, Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }

// nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
// </style>
