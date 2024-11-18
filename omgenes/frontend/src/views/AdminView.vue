<template>
  <div class="pa-4">
    <h1>All Users</h1>
    <v-data-table
      :headers="[
      {title: 'ID'},
      {title:'First Name'}, 
      {title:'Last Name'}, 
      {title: 'Email'},
      {title: 'Actions'}
      ]"
      :items="allUsers"
      class="elevation-1"
    >

    <template v-slot:item="{ item }">
      <tr>
        <td>{{ item.id }}</td>
        <td>{{ item.f_name }}</td>
        <td>{{ item.l_name }}</td>
        <td>{{ item.email }}</td>
        <td><v-btn v-if="item.email!='jmarias@up.edu.ph'" color="red" @click="this.deleteUser(item.id)">Delete</v-btn></td>
      </tr>
    </template>


    </v-data-table>

    <!-- <v-list-item v-for="user in allUsers" 
    :key="user.id">
        {{ user }}
    </v-list-item> -->

    <h1>All Variant Reads</h1>

    <v-data-table
      :headers="[
      {title:'ID'}, 
      {title:'Name'}, 
      {title: 'Reference Genome'},
      {title: 'VCF File'},
      {title: 'Actions'}
      ]"
      :items="allReads"
      class="elevation-1"
    >

    <template v-slot:item="{ item }">
      <tr>
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.genomeURL.split("/").pop() }}</td>
        <td>{{ item.variantURL.split("/").pop() }}</td>
        <td><v-btn color="red" @click="this.deleteRead(item.id)">Delete</v-btn></td>
      </tr>
    </template>
    </v-data-table>

    <!-- <v-list-item v-for="read in allReads" 
    :key="read.id">
        {{ read }}
    </v-list-item> -->

   <h1>All Variant Calls</h1>

    <v-data-table
      :headers="[
      {title:'ID', value: 'id'}, 
      {title:'Name', value: 'name'}, 
      {title: 'Reference Genome', value: 'referenceGenomeURL'},
      {title: 'Sample Genome', value: 'genomeURL'},
      {title: 'VCF File', value: 'vcfURL'},
      {title: 'Status', value: 'status'},
      {title: 'Actions'}
      ]"
      :items="allCalls"
      class="elevation-1"
    >

    <template v-slot:item="{ item }">
      <tr>
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.referenceGenomeURL.split("/").pop() }}</td>
        <td>{{ item.genomeURL.split("/").pop() }}</td>
        <td>{{ item.vcfURL==null ? "N/A" : item.vcfURL.split("/").pop()}}</td>
        <td>{{ item.status }}</td>
        <td><v-btn color="red" @click="this.deleteCall(item.id)">Delete</v-btn></td>
      </tr>

    </template>
    </v-data-table>

    <!-- <v-list-item v-for="call in allCalls" 
    :key="call.id">
        {{ call }}
    </v-list-item> -->
  </div>
</template>

<script>
import { onMounted, mounted, created } from 'vue'
import adminHandler from "@/api/admin"
import fileHandler from "@/api/file"
import callHandler from "@/api/call"

export default {
  name: 'AdminView',
  data(){
    return {
        allUsers: [],
        allReads: [],
        allCalls: []
      }
  },
  methods: {
    deleteRead(id){
      fileHandler.deleteRead(id).then((response)=>{
        this.$router.go(0);
      })
    },
    deleteCall(id){
      callHandler.deleteCall(id).then((response)=>{
        this.$router.go(0);
      })
    },
    deleteUser(id){
      adminHandler.deleteUser(id).then((response)=>{
        this.$router.go(0);
      })
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