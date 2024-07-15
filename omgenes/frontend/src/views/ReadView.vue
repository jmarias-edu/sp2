<template>
  <div>
    <v-card :title="`${this.name}`">
    </v-card>
    <v-btn @click="test">Test Values</v-btn>
    <v-btn @click="deleteRead">Delete Project</v-btn>
    <div id="igv-div"></div>
  </div>
</template>

<script>

import fileHandler from "@/api/file"
import { onMounted, mounted, updated, beforeRouteUpdate, created, beforeUpdate } from 'vue'
import {loadScript} from "vue-plugin-load-script";

export default {
  data() {
    return {
      genome: "",
      vcf: "",
      index: "",
      name: ""
    }
  },
  name: 'ReadView',
  props: ["id"],
  methods:{
    test(){
      console.log(this.id)
      console.log(this.genome)
      console.log(this.vcf)
      console.log(this.name)
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
                reference: {
                  fastaURL: response.data.reads.genomeURL,
                  indexed: false
                },
                tracks: [
                    {
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
      fileHandler.deleteRead(this.id)
      this.$router.push({path: "/"})
    }
  },
  created(){
    this.fetchRead()
  }

}
</script>