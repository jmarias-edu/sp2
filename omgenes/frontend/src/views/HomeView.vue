<template>
  <div>
    <v-card title="Welcome to OMGenes!" class="pa-4">
      
      <v-card-text> 
        OMGenes is a web application for viewing VCF files and creating them through a simple Variant Call script.
      </v-card-text>

      <v-card class="ma-4">
          <v-card-title>
            Testing Files
            <v-btn style="float: right;" color="info" href="https://drive.google.com/uc?export=download&id=14ClkiGhT5GNjY_Q6WQz4kU_UnNxcA80x">Download</v-btn>
          </v-card-title>
        <v-card-subtitle>Testing Files</v-card-subtitle>
      </v-card>

      <v-card-text>
      <pre>
Hi! If you are reading this, it means that hopefully you've agreed to become a tester for my webapp! (Yay!)

Like you, I want to keep the testing short and sweet for everyone so I'll boil down what needs to happen

Preparation
1. Login with your Google Account on the upper right
2. Download the testing files from the zip file above
3. Extract the zip file to access the files

Viewing existing VCF Files with Reference Genome
1. Open the Create New Read page from the Navigation Drawer on the left
2. Input a name for the Variant Call Read
3. Upload the Reference Genome File and the VCF File in the Variant Read Folder in their respective containers
4. Press Create
5. Click the newly created Variant Call Read to view

Creating new VCF File with a Reference and Sample Genome
1. Open the Create New Call page from the Navigation Drawer on the left
2. Input a name for the Variant Call
3. Upload the Reference Genome File and the Sample Genome File in the Variant Call Folder in their respective containers
4. Press Create
5. Click the newly created Variant Call
6. Press Run Call and wait for the server to finish processing
7. Restart when the prompt appears

Evaluation
After testing the different functions, please answer the evaluation form linked below! Thank you so much!
      </pre>
      </v-card-text>
      <v-btn target="_blank" href="https://forms.gle/dVRzW45ZKcfVH8RMA"  color="info">Evaluation Form</v-btn>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'HomeView'
}
</script>
