<template>
  <div class="">

    <v-card class="pa-4 w-100" color="info" style="display: none;">
      <v-card-text>
        <pre style="white-space: pre-wrap;">
<h3>Viewing the VCF File</h3>
You should now see the files you uploaded below as <b>downloadable files</b> and <b>displayed in the Genome Browser.</b>

<b>Zoom in the IGV Browser</b> to see the Reference Genome using the plus and minus buttons on the upper left of the IGV Browser. You may also <b>click on the blue squares</b> in the VCF File Track to see more details.

The reference genome and VCF File I provided for the test is from <b>Chromosome I of Yeast</b> (<i>Saccharomyces cerevisiae</i>)

You may proceed to testing the Variant Calling function by <b>pressing "Create New Call" on the left</b>
        </pre>
      </v-card-text>
    </v-card>

    <v-card  class="pa-4" >
        <v-card-title>
          <h3 style="float: left;">Genome Browser View</h3>
          <v-btn @click="deleteRead" style="float: right;" color="red">Delete VCF Read</v-btn>
        </v-card-title>
        
        <div id="igv-div"></div>

        <br>
        <v-card-title><h4>{{ this.name }} Files</h4></v-card-title>
        <v-card class="ma-4">
          <v-card-title>
            {{ this.genome.split("/").pop() }}
            <v-btn :href="this.genome" style="float: right;" color="info">Download</v-btn>
            </v-card-title>
          <v-card-subtitle>Reference Genome</v-card-subtitle>
        </v-card>
        <v-card class="ma-4">
          <v-card-title>
            {{ this.vcf.split("/").pop() }}
            <v-btn :href="this.vcf" style="float: right;" color="info">Download</v-btn>
          </v-card-title>
          <v-card-subtitle>VCF File</v-card-subtitle>
        </v-card>
        
    </v-card>

    

  </div>
</template>

<script>

import fileHandler from "@/api/file"
import { onMounted, mounted, updated, beforeRouteUpdate, created, beforeUpdate } from 'vue'
import {loadScript} from "vue-plugin-load-script";

export default {
  // inject: ["removeID"],
  data() {
    return {
      genome: "",
      vcf: "",
      index: "",
      name: ""
    }
  },
  name: 'ReadView',
  props: {
    id: Number
  },
  methods:{
    test(){
      console.log(this.id)
      console.log(this.genome)
      console.log(this.vcf)
      console.log(this.name)
      console.log(this.removeID)
    },
    fetchRead(){
      fileHandler.fetchRead(this.id).then(
        response => {
          this.genome = response.data.reads.genomeURL;
          this.vcf = response.data.reads.variantURL;
          this.name = response.data.reads.name;

          loadScript("https://cdn.jsdelivr.net/npm/igv@2.15.13/dist/igv.min.js").then(() => {
            var igvDiv = document.getElementById("igv-div");
            var options =
              {
                // genome: "sacCer3",
                genome: {
                  fastaURL: response.data.reads.genomeURL,
                  indexed: false,
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
                        "url": response.data.reads.variantURL
                    }
                ]
              };

            igv.createBrowser(igvDiv, options)
              .then(function (browser) {
                  console.log("Created IGV browser");
            })
          })
        }
      )
    },
    deleteRead(){
      // this.removeID(this.id);
      fileHandler.deleteRead(this.id).then(
        response=>{
          this.$router.push({path: "/"}).then(
            response =>{
              this.$router.go(0);
            }
          )
      })
    }
  },
  created(){
    this.fetchRead()
  }

}
</script>