<template>
  <div>
    <v-card :title="`${this.name} Files`" class="pa-4 w-100">
        <v-card class="ma-4">
          <v-card-title>
            {{ this.ref.split("/").pop() }}
            <v-btn :href="this.ref" style="float: right;">Download</v-btn>
            </v-card-title>
          <v-card-subtitle>Reference Genome</v-card-subtitle>
        </v-card>
        <v-card class="ma-4">
          <v-card-title>
            {{ this.genome.split("/").pop() }}
            <v-btn :href="this.genome" style="float: right;">Download</v-btn>
          </v-card-title>
          <v-card-subtitle>Target Genome</v-card-subtitle>
        </v-card>
        <v-card v-if="this.vcf!=null" class="ma-4">
          <v-card-title>
            {{ this.vcf.split("/").pop() }} 
            <v-btn :href="this.vcf" style="float: right;">Download</v-btn>
          </v-card-title>
          <v-card-subtitle>Reference Genome</v-card-subtitle>
        </v-card>
        <!-- <p><a v-bind:href="this.ref">Reference Genome</a></p>
        <p><a v-bind:href="this.genome">Target Genome</a></p>
        <p><a v-if="this.vcf!=null" v-bind:href="this.vcf">VCF File</a></p> -->
    </v-card>

    <v-card title="Genome Browser View" class="pa-4 w-100" v-if="this.vcf!=null">
      <div id="igv-div"></div>
    </v-card>

    <v-card title="Variant Call Settings" class="pa-4 w-100" v-if="this.vcf!=null">
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

                if (this.vcf!=null){
                  this.loadGenomeBrowser();
                }
            }
        )
    },
    runCall(){
      callHandler.runCall(this.id)
    },
    loadGenomeBrowser(){
      loadScript("https://cdn.jsdelivr.net/npm/igv@2.15.13/dist/igv.min.js").then(() => {
            var igvDiv = document.getElementById("igv-div");
            var options =
              {
                // genome: "sacCer3",
                genome: {
                  fastaURL: this.ref,
                  // indexed: false,
                  // indexURL: "http://localhost:8000/media/projects/user_1/16/genome.fa.fai"
                },
                tracks: [
                    { 
                      name: "Reference Genome",
                      type: 'sequence',
                      order: 0,
                      displayMode: 'EXPANDED',
                      visibilityWindow: 30000000,
                      height: 500,
                      color: '#3366cc',
                      fontSize: 30
                    },
                    {
                        "name": "VCF File",
                        "type": "variant",
                        "format": "vcf",
                        "url": this.vcf
                    }
                ]
              };

            igv.createBrowser(igvDiv, options)
              .then(function (browser) {
                  console.log("Created IGV browser");
            })
          })
    }
  },
  created(){
    this.fetchCall();
  }

}
</script>