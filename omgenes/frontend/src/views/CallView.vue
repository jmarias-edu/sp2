<template>
  <div>
    <v-card color="info" class="pa-4 w-100" style="display: none;">
      <v-card-text>
      <pre style="white-space: pre-wrap;">
<h3>Running the Variant Call</h3>
6. <b>Press Run Call</b> at the bottom of the page and wait for the server to finish processing
7. <b>Press "Ok"</b> to restart when the alert prompt appears

Once this page <b>reloads</b>, you will see the <b>uploaded files</b> and a <b>newly created VCF file</b> that you can download.

The <b>Genome Browser</b> will also present the <b>reference genome, vcf file, and alignment file</b> used in the Variant Call. <b>A log</b> of what happened during the <b>variant call</b> in the backend is also available below the genome browser.

After viewing the results, you may go access the evaluation form below!

<v-btn target="_blank" href="https://forms.gle/dVRzW45ZKcfVH8RMA">Evaluation Form</v-btn></pre>
      </v-card-text>
    </v-card>
    

    <v-card class="pa-4 w-100" v-if="this.vcf!=null">
      <v-card-title>
        <h3 style="float: left;">Genome Browser View</h3>
        <v-btn @click="deleteCall" style="float: right;" color="red">Delete Call</v-btn>
      </v-card-title>

      <div id="igv-div"></div>

      <v-card-text style="display: none;">
      <pre style="white-space: pre-wrap;">
<h3>About the Test Files</h3>
The reference and sample genome I provided in this test are from <b>COVID-19</b>, the <b>reference genome is the original COVID-19</b> virus and the <b>sample genome</b> is a strain of COVID that has the <b>D614G mutation</b> which caused a change in its spike protein that made it much more infectious.

You may see the <b>specific mutation</b> at the position 23404, copy <b>NC_045512v2:23,404</b> to the search bar in the IGV Genome Browser to see the mutation in the VCF File, you may click the <b>dark blue bar</b> at the position to see the <b>A->G mutation</b>.</pre>
      </v-card-text>

      <v-card-title><h4>{{ this.name }} Files</h4></v-card-title>
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

      <v-card-title><h4>Variant Call Log</h4></v-card-title>
      <pre class="logfile-display">{{ this.log }}</pre>
    </v-card>

    <v-card v-else class="pa-4 w-100">
      <v-card-title>
        <h3 style="float: left">Variant Call Settings</h3>
        <v-btn @click="deleteCall" style="float: right;" color="red">Delete Call</v-btn>
        <v-btn @click="runCall" class= "mr-2" style="float: right;" v-if="this.status!='Running'" color="info">Run Call</v-btn>
        <p style="float: right;" class="mr-2" v-else> Variant Call is currently running, please wait </p>
      </v-card-title>
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