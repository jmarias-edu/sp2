<template>
  <div>
    <v-card class="pa-2 my-1" title="About the Website" outlined>
      <v-card-text>
        OMGenes is a Web Application where you can view Reference Genomes and their VCF Files. You can also generate VCF files given a reference genome and a sample genome. It uses Snakemake as the workflow with various packages to run the Mapping, Indexing, Calling, et cetera to be able to run a simple Variant Call.
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1" title="About the Technology Stack">
      <v-card-text>
        Frontend: Vue.js<br>
        Backend: Django<br>
        Deployment: Digital Ocean, Name Silo, Traefik, Nginx, Docker<br>
        Variant Calling Workflow: Snakemake, Conda, BWA, Samtools, BCFtools<br>
        Genome Browser: IGV Genome Browser<br>
        Cookiecutter Django was used as a template for entire project
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1" title="About the Developer">
      <v-card-text>
        Hello! I am Jarem Thimoty M. Arias, currently undertaking BS Computer Science in UP Los Banos. I've always loved the aspect of Computer Science being applicable to many fields and Biology was a perfect field for me to explore. Coupled with the fact that Web Development isn't my strongest suite when it comes to Programming, it was a perfect way for me to explore new horizons and sharpen up my skills!
      </v-card-text>
      <v-card-text>
        Throughout the completion of this Special project I have learned many things about Genomics both in the Biology side and the Computer Science Side. From learning about Bioinformatics tools and the myriad of Databases that one can access Genetic Data to learning how to set-up deployment and creating a technology stack for specific Bioinformatics technologies.
      </v-card-text>
      <v-card-text>
        When I'm not programming, I enjoy playing Video Games, listening to Kpop, and playing with my cat. Thank you for taking the time to learn more about me!
      </v-card-text>
    </v-card>

    <v-card class="pa-2 my-1" title="Acknowledgements">
      <v-card-text> 
        I would like to share my deepest thanks for the people who has supported me throughout the creation of this Web Application for my Special Problem. Firstly, I would like to deeply thank my Advisor, Ma'am Mylah Rystie U. Anacleto whose expertise, support, and guidance has been invaluable throughout the process. Special thanks to my friends and colleagues in UPLB who have offered their advice, help, and support. And finally to my Family who has been supportive despite the various mishaps that happened throughout my journey.
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>