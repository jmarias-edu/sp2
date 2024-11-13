<template>
  <div class="pa-4">
    <v-toolbar-title><h5>All Users</h5></v-toolbar-title>

    <v-list-item v-for="user in allUsers" 
    :key="user.id">
        {{ user }}
    </v-list-item>

    <v-toolbar-title><h5>All Variant Reads</h5></v-toolbar-title>

    <v-list-item v-for="read in allReads" 
    :key="read.id">
        {{ read }}
    </v-list-item>

    <v-toolbar-title><h5>All Variant Calls</h5></v-toolbar-title>

    <v-list-item v-for="call in allCalls" 
    :key="call.id">
        {{ call }}
    </v-list-item>
  </div>
</template>

<script>
import { onMounted, mounted, created } from 'vue'
import adminHandler from "@/api/admin"

export default {
  name: 'AdminView',
  data(){
    return {
        allUsers: [],
        allReads: [],
        allCalls: []
      }
  },
  created(){
    adminHandler.fetchAllCalls().then((response)=>{
        console.log(response.data);
        this.allCalls = response.data.calls;
    });

    adminHandler.fetchAllReads().then((response)=>{
        console.log(response.data);
        this.allReads = response.data.reads;
    });

    adminHandler.fetchAllUsers().then((response)=>{
        console.log(response.data);
        this.allUsers = response.data.users;
    });
  }
}
</script>