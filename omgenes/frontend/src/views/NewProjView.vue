<template>
  <div>
    <v-card title="File Upload Test">
      <v-file-input v-model="file" label="Test File"></v-file-input>
      <v-btn @click="upload">Upload</v-btn>
    </v-card>

    <v-card title="">
      <v-text-field label="Project Name" v-model="name"></v-text-field>
      <v-file-input v-model="genome" label="Genome File"></v-file-input>
      <v-file-input v-model="vcf" label="VCF File"></v-file-input>
      <v-btn @click="createProj">Create</v-btn>
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
      name: ""
    }
  },
  methods: {
    upload() {
      console.log("Here!");
      const formData = new FormData();
      formData.append('file', this.file);
      fileHandler.uploadFile(formData);
    },

    createProj(){
      // Add Error detection to input
      const genomeFile = new FormData();
      const vcfFile = new FormData();
      genomeFile.append("file", this.genome)
      vcfFile.append("file", this.vcf)
      const genomeFileName = this.genome.name
      const vcfFileName = this.vcf.name
      console.log(this.name)
      fileHandler.uploadFile(genomeFile).then(
        response => {
          fileHandler.uploadFile(vcfFile).then(
            response => {
              
              //fix filename for link
              const formData = new FormData();
              formData.append('name', this.name)
              formData.append('genomeURL', "http://localhost:8000/media/uploads/"+ genomeFileName)
              formData.append('variantURL', "http://localhost:8000/media/uploads/"+ vcfFileName)
              formData.append('token', Cookies.get('authtoken'))
              console.log(formData)
              fileHandler.createReads(formData).then(response =>{console.log(response)})
            }
          )
        }
      )
    }
  }
}
</script>
