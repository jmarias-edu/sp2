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
            genome: "sacCer3",
            tracks: [
                {
                    "type": "variant",
                    "format": "vcf",
                    "url": "http://localhost:8000/media/uploads/all.vcf"
                }
            ]
        };

        igv.createBrowser(igvDiv, options)
          .then(function (browser) {
              console.log("Created IGV browser");
        })
    })
  
</script>