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
      name: ""
    }
  },
  methods: {
    upload() {
      console.log("Here!");
      const formData = new FormData();
      formData.append('file', this.file);
      fileHandler.uploadFile(formData).then(
        response => {
          console.log(response);
        }
      )
    },

    createProj(){
      // Add Error detection to input
      const genomeFile = new FormData();
      const vcfFile = new FormData();
      genomeFile.append("file", this.genome)
      vcfFile.append("file", this.vcf)
      const genomeFileName = ""
      const vcfFileName = ""
      console.log(this.name)

      fileHandler.uploadFile(genomeFile).then(
        response1 => {
          fileHandler.uploadFile(vcfFile).then(
            response2 => {
              const formData = new FormData();
              formData.append('name', this.name)
              formData.append('genomeURL', "http://localhost:8000" + response1.data.file)
              formData.append('variantURL', "http://localhost:8000" + response2.data.file)
              formData.append('token', Cookies.get('authtoken'))
              console.log(formData)
              fileHandler.createReads(formData).then(response =>{console.log(response)})
            }
          )
        }
      )
    },
    createProject(){
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
      

      fileHandler.createReads(formData).then(
        response1 => {
          console.log(response1.data)
          genomeFile.append("projid", response1.data.id);
          vcfFile.append("projid", response1.data.id);

          fileHandler.uploadProjectFile(genomeFile).then(
            response2 => {
              console.log(response2)

              fileHandler.uploadProjectFile(vcfFile).then(
                response3 => {
                  console.log(response3)
                  updateData.append("genome", "http://localhost:8000" + response2.data.file)
                  updateData.append("vcf", "http://localhost:8000" + response3.data.file)
                  updateData.append("readID", response1.data.id)

                  fileHandler.updateReadsLinks(updateData).then(
                    response4 => {
                      console.log(response4);
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
