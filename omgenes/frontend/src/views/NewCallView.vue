<template>
  <div>

    <v-card title="Create New Variant Call Job" class="pa-4">
      <v-form ref="form" v-model="valid">
        <v-text-field :rules="textRules" label="Variant Call" v-model="name" required></v-text-field>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="ref" label="Reference Genome File" required></v-file-input>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="genome" label="Genome to Compare" required></v-file-input>
        <v-btn @click="createCall">Create</v-btn>
      </v-form>
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
            updateData.append("genome", "http://localhost:8000" + response3.data.file)
            updateData.append("ref", "http://localhost:8000" + response2.data.file)
            updateData.append("callid", response1.data.id)
            callHandler.updateCallFile(updateData).then(
              response4 => {
                console.log(response4);
                this.$router.push({path: "/"});
                this.$router.go(0);
              }
            )
          })
        })
      })
    }
  }
}

</script>
