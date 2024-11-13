<template>
  <div>

    <v-card  class="pa-4">
      <v-card-title><h3>Create New Variant Call</h3></v-card-title>
      <v-form ref="form" v-model="valid">
        <v-text-field :rules="textRules" label="Variant Call Name" v-model="name" required></v-text-field>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="ref" label="Reference Genome File (.fa, .fastq, .fasta)" required></v-file-input>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="genome" label="Sample Genome to Call (.fa, .fastq, .fasta)" required></v-file-input>
        <v-btn @click="createCall" color="info">Create</v-btn>
      </v-form>
    </v-card>

    <v-card color="info" class="pa-4 w-100" style="display: none;">
      <v-card-text>
      <pre style="white-space: pre-wrap;">
<h3>Creating new VCF File with a Reference and Sample Genome</h3>
1. <b>Open</b> the <b>Create New Call</b> page from the Navigation Drawer on the left
2. <b>Input</b> a <b>name</b> for the Variant Call
3. <b>Upload</b> the <b>Reference Genome File</b> and the <b>Sample Genome File</b> from the Variant Call Folder in their respective containers
4. <b>Press Create</b></pre>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import callHandler from "@/api/call"
import Cookies from 'js-cookie'

export default {
  name: "NewCallView",
  data() {
    return {
      ref: null,
      genome: null,
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
    createCall(){
      this.$refs.form.validate();
      if (!this.valid) {
        alert('Please fill in all required fields.');
        return; // Exit if the form is invalid
      }

      const callData = new FormData();
      const refFile = new FormData();
      const genomeFile = new FormData();
      const updateData = new FormData();

      callData.append("token", Cookies.get('authtoken'));
      callData.append("name", this.name);

      refFile.append("token", Cookies.get('authtoken'))
      genomeFile.append("token", Cookies.get('authtoken'))

      callHandler.createCall(callData)
      .then((response1)=>{
        refFile.append("callid", response1.data.id);
        genomeFile.append("callid", response1.data.id);

        refFile.append("file", this.ref);
        genomeFile.append("file", this.genome);

        callHandler.uploadCallFile(refFile)
        .then((response2)=>{
          callHandler.uploadCallFile(genomeFile)
          .then((response3)=>{
            updateData.append("genome",process.env.VUE_APP_BACKEND_URL + response3.data.file)
            updateData.append("ref", process.env.VUE_APP_BACKEND_URL + response2.data.file)
            updateData.append("callid", response1.data.id)
            callHandler.updateCallFile(updateData).then(
              response4 => {
                console.log(response4);
                this.$router.push({path: "/calls/"+response1.data.id}).then(()=>{
                        window.location.reload();
                      });
              }
            )
          })
        })
      })
    }
  }
}

</script>
