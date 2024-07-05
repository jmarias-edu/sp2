<template>
  <div>
    <v-card title="File Upload">
      <v-file-input v-model="file" label="Test File"></v-file-input>
      <!-- <v-file-input label="Index File"></v-file-input> -->
      <!-- <v-file-input label="VCF File"></v-file-input>-->
      <v-btn @click="upload">Upload</v-btn>
    </v-card>
  </div>
</template>

<script>

import fileHandler from "@/api/file"

export default {
  name: 'NewProjView',
  data() {
    return {
      file: null,
    }
  },
  methods: {
    upload() {
      console.log("Here!");
      const formData = new FormData();
      formData.append('file', this.file);
      fileHandler.uploadFile(formData);
    }
  }
}
</script>
