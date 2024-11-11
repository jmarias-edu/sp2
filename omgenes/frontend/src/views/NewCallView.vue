<template>
  <div>

    <v-card title="Create New Variant Call" class="pa-4">
      <v-form ref="form" v-model="valid">
        <v-text-field :rules="textRules" label="Variant Call Name" v-model="name" required></v-text-field>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="ref" label="Reference Genome File" required></v-file-input>
        <v-file-input :rules="fileRules" accept=".fa,.fasta,.fastq" v-model="genome" label="Sample Genome to Call" required></v-file-input>
        <v-btn @click="createCall">Create</v-btn>
      </v-form>
    </v-card>

    <v-card title="Variant Call Creation instructions" color="info" class="pa-4 w-100">
      <v-card-text>
      <pre style="white-space: pre-wrap;">
Creating new VCF File with a Reference and Sample Genome
1. Open the Create New Call page from the Navigation Drawer on the left
2. Input a name for the Variant Call
3. Upload the Reference Genome File and the Sample Genome File in the Variant Call Folder in their respective containers
4. Press Create
5. Click on the name of the newly created Variant Call
      </pre>
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
