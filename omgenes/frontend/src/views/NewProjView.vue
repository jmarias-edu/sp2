<template>
  <div>
    <!-- <v-card title="File Upload Test">
      <v-file-input v-model="file" label="Test File"></v-file-input>
      <v-btn @click="upload">Upload</v-btn>
    </v-card> -->

    <v-card title="Create New VCF Read" class="pa-4">
      <v-text-field :rules="textRules" label="Project Name" v-model="name" required></v-text-field >
      <v-file-input :rules="fileRules" v-model="genome" label="Genome File" required></v-file-input>
      <v-file-input :rules="fileRules" v-model="vcf" label="VCF File" required></v-file-input>
      <v-btn @click="createProject">Create</v-btn>
    </v-card>

  </div>
</template>

<script>

import fileHandler from "@/api/file"
import Cookies from 'js-cookie'

export default {
  name: 'NewProjView',
  data() {
    return {
      file: null,
      genome: null,
      vcf: null,
      name: "",
      textRules: [
        v => !!v || 'Text input is required',
      ],
      fileRules: [
        v => !!v || 'File input is required',
      ],
    }
  },
  methods: {

    createProject(){
      // if (!this.$refs.form.validate()) {
      //   alert('Please fill in all required fields.');
      //   return; // Exit if the form is invalid
      // }

      const genomeFile = new FormData();
      const vcfFile = new FormData();
      const formData = new FormData();
      const updateData = new FormData();

      genomeFile.append("file", this.genome)
      vcfFile.append("file", this.vcf)
      formData.append("name", this.name)

      formData.append("token", Cookies.get('authtoken'))
      genomeFile.append("token", Cookies.get('authtoken'))
      vcfFile.append("token", Cookies.get('authtoken'))
      fileHandler.createReads(formData)
      .then(
        response1 => {
          console.log(response1.data)
          genomeFile.append("projid", response1.data.id);
          vcfFile.append("projid", response1.data.id);

          fileHandler.uploadProjectFile(genomeFile)
      .then(
          response2 => {
            console.log(response2)
            fileHandler.uploadProjectFile(vcfFile)
      .then(
          response3 => {
            console.log(response3)
            updateData.append("genome", "http://localhost:8000" + response2.data.file)
            updateData.append("vcf", "http://localhost:8000" + response3.data.file)
            updateData.append("readID", response1.data.id)

            fileHandler.updateReadsLinks(updateData).then(
              response4 => {
                console.log(response4);
                this.$router.push({path: "/"});
                this.$forceUpdate();
              }
            )
          }
              )
            }
          )
        }
      )
    }
  }
}
</script>
