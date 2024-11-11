<template>
  <div>
    <v-card title="Welcome to OMGenes!" class="pa-4">

      <v-card class="ma-4">
          <v-card-title>
            Testing Files
            <v-btn style="float: right;" color="info" href="https://drive.google.com/uc?export=download&id=14ClkiGhT5GNjY_Q6WQz4kU_UnNxcA80x">Download</v-btn>
          </v-card-title>
        <v-card-subtitle>Testing Files</v-card-subtitle>
      </v-card>

      <v-card-text>
      <pre style="white-space: pre-wrap;">
Hi! I am Jarem Thimoty M. Arias, currently a student in the University of the Philippines Los Banos under BS Computer Science and finishing up my Special Problem which is the website you currently on now!

If you are reading this, it means that hopefully you've agreed to become a tester for my webapp! (Yay!)

Like you, I want to keep the testing short and sweet for everyone so I'll boil down what needs to happen:

OMGenes is a website for viewing and creating VCF Files through an open-source Genome Browser and Variant Caller. I have provided the files needed in the zip file above for testing, you just have to follow the rest of the instructions below (It'll be quick I promise ^^)

For testing, I will be providing Reference Genomes, VCF Files, and Sample Genomes for Yeast and COVID-19 for testing.

Below are the full instructions, but each step will have a blue section to guide you!

Preparation
1. Sign-up/Log-in with your Google Account on the upper right by the navigation bar
2. Download the testing files from the zip file above
3. Extract the zip file to access the files

Viewing existing VCF Files with Reference Genome
1. Open the Create New Read page from the Navigation Drawer on the left.
2. Input a name for the Variant Call Read.
3. Upload the Reference Genome File and the VCF File in the Variant Read Folder in their respective containers.
4. Press Create.
5. Click the name of the newly created Variant Call Read to view your VCF File in the IGV Genome Browser.

Creating new VCF File with a Reference and Sample Genome
1. Open the Create New Call page from the Navigation Drawer on the left
2. Input a name for the Variant Call
3. Upload the Reference Genome File and the Sample Genome File in the Variant Call Folder in their respective containers
4. Press Create
5. Click on the name of the newly created Variant Call
6. Press Run Call at the bottom of the page and wait for the server to finish processing
7. Press "Ok" to restart when the alert prompt appears

Evaluation
After testing the different functions, please answer the evaluation form linked below! Thank you so much! If you have your own Genome Files and VCF files you'd like to try out feel free to use OMGenes!

If you have any questions, you may contact me at jmarias@up.edu.ph
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
