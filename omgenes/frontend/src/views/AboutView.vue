<template>
  <div class="about">
    <div id="igv-div"></div>
  </div>
</template>

<script setup>
  import {loadScript} from "vue-plugin-load-script";
  loadScript("https://cdn.jsdelivr.net/npm/igv@2.15.5/dist/igv.min.js")
    .then(() => {
      var igvDiv = document.getElementById("igv-div");
      var options =
        {
            genome: "hg38",
            locus: "chr8:127,736,588-127,739,371",
            tracks: [
                {
                    "name": "HG00103",
                    "url": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram",
                    "indexURL": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram.crai",
                    "format": "cram"
                }
            ]
        };

        igv.createBrowser(igvDiv, options)
          .then(function (browser) {
              console.log("Created IGV browser");
        })
    })
  
</script>