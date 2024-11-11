<template>
  <div>
    <!-- <v-card title="File Upload Test">
      <v-file-input v-model="file" label="Test File"></v-file-input>
      <v-btn @click="upload">Upload</v-btn>
    </v-card> -->

    <v-card title="Create New VCF Read" class="pa-4">
      <v-form ref="form" v-model="valid">
        <v-text-field :rules="textRules" label="VCF Read Name" v-model="name" required></v-text-field >
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="genome" label="Reference Genome File" required></v-file-input>
        <v-file-input :rules="fileRules" accept=".vcf" v-model="vcf" label="VCF File" required></v-file-input>
        <v-btn @click="createProject">Create</v-btn>
      </v-form>
    </v-card>


    <v-card title="VCF Read Instructions" color="info" class="pa-4 w-100">
      <v-card-text>
      <pre style="white-space: pre-wrap;">
Viewing existing VCF Files with Reference Genome
1. Open the Create New Read page from the Navigation Drawer on the left.
2. Input a name for the Variant Call Read.
3. Upload the Reference Genome File and the VCF File in the Variant Read Folder in their respective containers.
4. Press Create.
5. Click the name of the newly created Variant Call Read to view your VCF File in the IGV Genome Browser.
      </pre>
      </v-card-text>
    </v-card>

  </div>
</template>

<script>

import fileHandler from "@/api/file"
import Cookies from 'js-cookie'
// import { ref } from "vue"

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
        v => !!v || 'File is required',
        v => (v && v.length > 0) || 'File is required',
      ],
      valid: false,
    }
  },
  methods: {
    onFileChange(){

    },
    createProject(){
      // alert("Test")
      this.$refs.form.validate();
      if (!this.valid) {
        alert('Please fill in all required fields.');
        return;
      }

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
              // console.log(response2)
              fileHandler.uploadProjectFile(vcfFile).then(
                response3 => {
                  // console.log(response3)
                  updateData.append("genome", process.env.VUE_APP_BACKEND_URL + response2.data.file)
                  updateData.append("vcf", process.env.VUE_APP_BACKEND_URL + response3.data.file)
                  updateData.append("readID", response1.data.id)
                  fileHandler.updateReadsLinks(updateData).then(
                    response4 => {
                      console.log(response4);
                      this.$router.push({path: "/"});
                      this.$router.go(0);
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
