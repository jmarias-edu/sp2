<template>
  <div>

    <v-card title="">
      <v-text-field label="Variant Call" v-model="name"></v-text-field>
      <v-file-input v-model="ref" label="Reference Genome File"></v-file-input>
      <v-file-input v-model="genome" label="Genome to Compare"></v-file-input>
      <v-btn @click="createProject">Create</v-btn>
    </v-card>

  </div>
</template>

<script>

export default {
  name: "NewCallView",
  data() {
    return {
      ref: null,
      genome: null,
      name: ""
    }
  },
  methods(){

  }
}

</script>
