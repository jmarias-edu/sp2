<template>
  <div class="pa-4">
    <v-card class="pa-2 my-1" outlined>
      <v-card-title><h3>About the Website</h3></v-card-title>
      <v-card-text>
        <b>OMGenes</b> is a Web Application where you can <b>view Reference Genomes and their VCF Files.</b> You can also <b>generate VCF files given a reference genome and a sample genome</b>. It uses <b>Snakemake</b> as the workflow with various packages to run the <b>Mapping, Indexing, Calling, et cetera</b> to be able to <b>run a simple Variant Call</b>.
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1">
      <v-card-title><h3>About the Technology Stack</h3></v-card-title>
      <v-card-text>
        <b>Frontend:</b> Vue.js<br>
        <b>Backend:</b> Django<br>
        <b>Deployment:</b> Digital Ocean, Name Silo, Traefik, Nginx, Docker<br>
        <b>Variant Calling Workflow:</b> Snakemake, Conda, BWA, Samtools, BCFtools<br>
        <b>Genome Browser:</b> IGV Genome Browser<br>
        <b>Cookiecutter Django</b> was used as a template for entire project
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1">
      <v-card-title><h3>About the Developer</h3></v-card-title>
      <v-card-text>
        Hello! I am <b>Jarem Thimoty M. Arias</b>, currently undertaking <b>BS Computer Science in UP Los Banos</b>. I've always loved the aspect of Computer Science being applicable to many fields and <b>Biology was a perfect field for me to explore</b>. Coupled with the fact that Web Development isn't my strongest suite when it comes to Programming, it was a perfect way for me to explore new horizons and sharpen up my skills!
        <br><br>
        Throughout the completion of this Special project I have learned many things about Genomics both in the Biology side and the Computer Science Side. From learning about Bioinformatics tools and the myriad of Databases that one can access Genetic Data to learning how to set-up deployment and creating a technology stack for specific Bioinformatics technologies.
        <br><br>
        When I'm not programming, I enjoy playing Video Games, listening to Kpop, and playing with my cat. Thank you for taking the time to learn more about me!
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1">
      <v-card-title><h3>Acknowledgements</h3></v-card-title>
      <v-card-text> 
        I would like to share <b>my deepest thanks</b> for the people who has supported me throughout the creation of this Web Application for my Special Problem. Firstly, I would like to deeply thank my <b>Advisor, Ma'am Mylah Rystie U. Anacleto</b> whose expertise, support, and guidance has been invaluable throughout the process. Special thanks to my <b>friends and colleagues</b> in UPLB who have offered their advice, help, and support. And finally to my <b>Family</b> who has been supportive despite the various mishaps that happened throughout my journey.
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>