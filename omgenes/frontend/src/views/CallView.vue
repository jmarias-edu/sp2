<template>
  <div>
    <v-card title="Running the Variant Call" color="info" class="pa-4 w-100">
      <v-card-text>
      <pre style="white-space: pre-wrap;">
Creating new VCF File with a Reference and Sample Genome
6. Press Run Call at the bottom of the page and wait for the server to finish processing
7. Press "Ok" to restart when the alert prompt appears

Once this page reloads, you will see the uploaded files and a newly created VCF file that you can download.

The Genome Browser will also present the reference genome, vcf file, and alignment file used in the Variant Call. A log of what happened during the variant call in the backend is also available below the genome browser.

After viewing the results, you may go back to the home page to answer the evaluation form! ^^
      </pre>
      </v-card-text>
    </v-card>
    <v-card :title="`${this.name} Files`" class="pa-4 w-100">
        <v-card class="ma-4">
          <v-card-title>
            {{ this.ref.split("/").pop() }}
            <v-btn :href="this.ref" style="float: right;" color="info">Download</v-btn>
            </v-card-title>
          <v-card-subtitle>Reference Genome</v-card-subtitle>
        </v-card>
        <v-card class="ma-4">
          <v-card-title>
            {{ this.genome.split("/").pop() }}
            <v-btn :href="this.genome" style="float: right;" color="info">Download</v-btn>
          </v-card-title>
          <v-card-subtitle>Target Genome</v-card-subtitle>
        </v-card>
        <v-card v-if="this.vcf!=null" class="ma-4">
          <v-card-title>
            {{ this.vcf.split("/").pop() }} 
            <v-btn :href="this.vcf" style="float: right;" color="info">Download</v-btn>
          </v-card-title>
          <v-card-subtitle>Reference Genome</v-card-subtitle>
        </v-card>
    </v-card>

    <v-card title="Genome Browser View" class="pa-4 w-100" style="height: 600px;" v-if="this.vcf!=null">
      <div id="igv-div"></div>

      <v-card-text>
      <pre style="white-space: pre-wrap;">

About the Variant Call Test files:
The reference and sample genome I provided in this test are from COVID-19, the reference genome is the original COVID-19 virus and the sample genome is a strain of COVID that has the D614G mutation which caused a change in its spike protein that made it much more infectious.

You may see the specific variant at the position 23404, copy "NC_045512v2:23,404" to the search bar in the IGV Genome Browser to see the mutation in the VCF File, you may click the blue bar at the position to see the A->G mutation.
      </pre>
      </v-card-text>
    </v-card>

    <v-card title="Variant Call Log" class="pa-4 w-100" v-if="this.vcf!=null">
      <pre class="logfile-display">{{ this.log }}</pre>
    </v-card>

    <v-card title="Variant Call Settings" class="pa-4 w-100">



      <v-btn @click="deleteCall" style="float: right;" color="red">Delete Call</v-btn>
      <v-btn @click="runCall" style="float: right;" v-if="this.status!='Running'" color="info">Run Call</v-btn>
      <p style="float: right;" v-else> Call is currently running, please wait </p>
    </v-card>
  </div>
</template>

<script>

import callHandler from "@/api/call"
import { onMounted, mounted, updated, beforeRouteUpdate, created, beforeUpdate, } from 'vue'
import {loadScript} from "vue-plugin-load-script";

export default {
  data() {
    return {
      genome: "",
      ref: "",
      index: "",
      name: "",
      vcf: "",
      logfile: "",
      log: "",
      polling: null,
      status: "",
      bam: "",

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
                this.logfile = response.data.calls.log;
                this.status = response.data.calls.status;
                this.bam = process.env.VUE_APP_API_URL + "media/" + response.data.calls.folder + "sorted_reads/sorted.bam";
                console.log(this.bam);

                if (this.vcf!=null){
                  this.loadGenomeBrowser();
                  this.fetchLogfile();
                }
            }
        )
    },
    runCall(){
      callHandler.runCall(this.id);
      this.startChecking();
      this.status = "Running";
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
                      "name": "Sorted Sample Reads",
                      "type": "alignment",
                      "format": "bam",
                      "url": this.bam,
                      "indexURL": this.bam + ".bai",
                      "height": 50
                    },
                    {
                      "name": "VCF File",
                      "type": "variant",
                      "format": "vcf",
                      "url": this.vcf,
                      "height": 100
                    }
                ]
              };

            igv.createBrowser(igvDiv, options)
              .then(function (browser) {
                  console.log("Created IGV browser");
            })
          })
    },
    async fetchLogfile() {
      try {
        const response = await fetch(this.logfile); // Adjust the endpoint as needed
        if (!response.ok) {
          throw new Error('Failed to fetch logfile');
        }
        const data = await response.text();
        this.log = data;

      } catch (error) {
        console.error('Failed to fetch logfile:', error);
      }
    },

    startChecking(){
      if(this.polling){
        clearInterval(this.polling)
      }
      this.polling = setInterval(()=>{
        this.checkIfDone();
      }, 1000)
    },
    async checkIfDone(){
      try{
        callHandler.fetchCall(this.id).then(
          response =>{
            if(response.data.calls.status == "Completed"){
              clearInterval(this.polling)
              alert("The Variant Call run is finished, please refresh the browser to see the results:>");
              this.$router.go(0);
            }
            else if(response.data.calls.status == "Failed"){
              clearInterval(this.polling)
              alert("The Variant Call run failed, please refresh the browser to try again :<");
              this.$router.go(0);
            }
          }
        )
      }
      catch{

      }
    }
  },
  created(){
    this.fetchCall();
    // console.log(process.env.VUE_APP_BACKEND_URL);
  }

}
</script>

<style scoped>
.logfile-display {
  white-space: pre-wrap; /* Preserves formatting */
  background-color: #f5f5f5;
  padding: 1rem;
  border: 1px solid #ccc;
  max-height: 400px; /* Limit the height */
  overflow-y: auto; /* Enable scrolling */
}
</style>