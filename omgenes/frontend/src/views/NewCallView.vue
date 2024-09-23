<template>
  <div>

    <v-card title="Create New Variant Call Job" class="pa-4">
      <v-text-field :rules="textRules" label="Variant Call" v-model="name" required></v-text-field>
      <v-file-input :rules="fileRules" v-model="ref" label="Reference Genome File" required></v-file-input>
      <v-file-input :rules="fileRules" v-model="genome" label="Genome to Compare" required></v-file-input>
      <v-btn @click="createCall">Create</v-btn>
    </v-card>

  </div>
</template>

<script>
import callHandler from "@/api/call"

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
        v => !!v || 'File input is required',
      ],
    }
  },
  methods: {
    createCall(){
      callHandler.createCall()
      .then((response)=>{

      })
    }
  }
}

</script>
