<template>
  <div class="d-flex">
    <v-card :title="`${this.name}`" class="pa-4 flex-grow-1">
        <a v-bind:href="this.ref">Reference Genome</a>
        <a v-bind:href="this.genome">Target Genome</a>
        <a v-if="this.vcf!=null" v-bind:href="this.vcf">VCF File</a>
        <v-btn @click="deleteCall" style="float: right;">Delete Call</v-btn>
        <v-btn @click="runCall" style="float: right;">Run Call</v-btn>
    </v-card>
  </div>
</template>

<script>

import callHandler from "@/api/call"
import { onMounted, mounted, updated, beforeRouteUpdate, created, beforeUpdate } from 'vue'
import {loadScript} from "vue-plugin-load-script";

export default {
  data() {
    return {
      genome: "",
      ref: "",
      index: "",
      name: "",
      vcf: ""
    }
  },
  name: 'CallView',
  props: {
    id: Number
  },
  methods:{
    deleteCall(){
      callHandler.deleteCall(this.id).then(
        response =>{
            this.$router.push({path: "/"}).then(
              response=>{
                this.$router.go(0);
          })
        }
      )
    },
    fetchCall(){
        callHandler.fetchCall(this.id).then(
            response => {
                console.log(response)
                this.name = response.data.calls.name;
                this.ref = response.data.calls.referenceGenomeURL;
                this.genome = response.data.calls.genomeURL;
                this.vcf = response.data.calls.vcfURL;
            }
        )
    },
    runCall(){
      callHandler.runCall(this.id)
    }
  },
  created(){
    this.fetchCall();
  }

}
</script>