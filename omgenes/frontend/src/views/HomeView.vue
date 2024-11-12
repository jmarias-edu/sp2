<template>
  <div>
    <v-card class="pa-4">

      <v-card-text>
      <pre style="white-space: pre-wrap;">

<h1>Look Here!</h1>
Hi! I am <b>Jarem Thimoty M. Arias</b>, currently a student in the University of the Philippines Los Banos under BS Computer Science and finishing up my Special Problem which is the website you currently on now!

If you are reading this, it means that hopefully you've agreed to become a tester for my webapp! (Yay!)

Like you, I want to <b>keep the testing short and sweet</b> for everyone so I'll boil down what needs to happen:

OMGenes is a website for <b>viewing and creating VCF Files</b> through an open-source <b>Genome Browser and Variant Caller</b>. I have provided the files needed in the <b>zip file below</b> for testing, you just have to follow the rest of the instructions below (It'll be quick I promise ^^)

For testing, I will be providing Reference Genomes, VCF Files, and Sample Genomes for Yeast and COVID-19 for testing.

<v-btn color="info" href="https://drive.google.com/uc?export=download&id=14ClkiGhT5GNjY_Q6WQz4kU_UnNxcA80x">Test Files Download</v-btn>


Below are the full instructions, but each page of the site will have a blue section to guide you!

<h3>Preparation</h3>
1. <b>Sign-up/Log-in</b> with your Google Account on the <b>upper right of the navigation bar</b>
2. <b>Download</b> the <b>testing files</b> from the blue button above
3. <b>Extract</b> the <b>zip file</b> using your preferred method to access the files

<h3>Viewing existing VCF Files with Reference Genome</h3>
1. <b>Open</b> the <b>Create New Read page</b> from the Navigation Drawer on the left.
2. <b>Input</b> a <b>name</b> for the Variant Call Read.
3. <b>Upload</b> the <b>Reference Genome File</b> and the <b>VCF File</b> from the Variant Read Folder in their respective containers.
4. <b>Press Create</b>.
5. <b>Click</b> the name of the <b>newly created Variant Call Read</b> to view your VCF File in the IGV Genome Browser.

<h3>Creating new VCF File with a Reference and Sample Genome</h3>
1. <b>Open</b> the <b>Create New Call</b> page from the Navigation Drawer on the left
2. <b>Input</b> a <b>name</b> for the Variant Call
3. <b>Upload</b> the <b>Reference Genome File</b> and the <b>Sample Genome File</b> from the Variant Call Folder in their respective containers
4. <b>Press Create</b>
5. <b>Click</b> on the <b>name</b> of the newly created Variant Call
6. <b>Press Run Call</b> at the bottom of the page and wait for the server to finish processing
7. <b>Press "Ok"</b> to restart when the alert prompt appears

<h3>Evaluation</h3>
After testing the different functions, please answer the evaluation form linked below! Thank you so much! If you have your own Genome Files and VCF files you'd like to try out feel free to use OMGenes!

If you have any questions, you may contact me at <b>jmarias@up.edu.ph</b>
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
