<template>
  <v-card class="pa-4">
    <v-card-title><h3>Sample VCF view of a saccharomyces cerevisiae VCF file using IGV Genome Browser</h3></v-card-title>
    <div id="igv-div" style="z-index: 100; position: relative;"></div>
  </v-card>
</template>

<script setup>
  import {loadScript} from "vue-plugin-load-script";
  loadScript("https://cdn.jsdelivr.net/npm/igv@2.15.5/dist/igv.min.js")
    .then(() => {
      var igvDiv = document.getElementById("igv-div");
      var options =
        {
            genome: "sacCer3",
            tracks: [
                {
                    "type": "variant",
                    "format": "vcf",
                    "url": "https://api.omgenes.click/media/uploads/all.vcf"
                }
            ]
        };

        igv.createBrowser(igvDiv, options)
          .then(function (browser) {
              console.log("Created IGV browser");
        })
    })
  
</script>