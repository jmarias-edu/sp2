<template>
  <div>
    <v-card class="pa-4 w-100">
        <v-card-title><h3>Snakemake Workflow</h3></v-card-title>
        <v-card-text>
Below is the <b>Snakemake workflow</b> used to create the VCF Files from a reference and sample genome. It makes use of a <b>simple alignment-based process</b> to create VCF files. <br><br>
This workflow is run in a <b>Conda Environment with BWA, BCFTools, and Samtools</b> which has various tools needed in the different steps of the Variant Call. <br><br>
The variant call is done through <b>"rules"</b> done in the order that you see above, and a simple explanation of the process is below:<br>
1. <b>Index files</b> for the reference genomes are created using <b>BWA</b><br>
2. Using the created index files, the sample genome is then <b>mapped to the reference genome</b> using <b>BWA and Samtools</b><br>
3. The map of the sample genome is then <b>sorted</b> using <b>Samtools</b><br>
4. The <b>sorted map</b> of the sample genome is then <b>indexed using Samtools</b><br>
5. Finally, using the sorted map of the sample genome and the reference genome, <b>BCFTools then runs the final Variant Call</b><br>
<br>
This workflow was based off the <b>Tutorial Workflow</b> from Snakemake but adjusted to <b>add the indexing for the reference genome and dynamicity of files</b>.
    </v-card-text>

      <pre class="logfile-display">
rule all:
  input:
      vcf=f"{config["target"]}.vcf"

rule refIndex:
    input:
        ref=config["ref"]
    output:
        "{ref}.amb",
        "{ref}.ann",
        "{ref}.bwt",
        "{ref}.pac",
        "{ref}.sa"
    shell:
        """
            bwa index {input}
        """

rule map:
    input:
        ref=config["ref"],
        target=config["target"],
        index=[ f"{config["ref"]}.amb",
                f"{config["ref"]}.ann",
                f"{config["ref"]}.bwt",
                f"{config["ref"]}.pac",
                f"{config["ref"]}.sa"
        ]
    output:
        f"{config["folder"]}/mapped_reads/mapped.bam"
    shell:
        """
        bwa mem {input.ref} {input.target} | samtools view -Sb - > {output}
        """

rule sort:
    input:
        f"{config["folder"]}/mapped_reads/mapped.bam"
    output:
        f"{config["folder"]}/sorted_reads/sorted.bam"
    shell:
        "samtools sort -T ./sorted_reads/target.sample "
        "-O bam {input} > {output}"

rule index:
    input:
        f"{config["folder"]}/sorted_reads/sorted.bam"
    output:
        f"{config["folder"]}/sorted_reads/sorted.bam.bai"
    shell:
        "samtools index {input}"

rule variant_calling:
    input:
        ref=config["ref"],  # Reference genome
        bam=f"{config["folder"]}/sorted_reads/sorted.bam",
        bai=f"{config["folder"]}/sorted_reads/sorted.bam.bai"
    output:
        vcf=f"{config["target"]}.vcf"
    shell:
        """
        bcftools mpileup -Ou -f {input.ref} {input.bam} | \
        bcftools call -mv -Ov -o {output.vcf}
        """

      </pre>

    
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'WorkflowView'
}
</script>

<style scoped>
.logfile-display {
  white-space: pre-wrap; /* Preserves formatting */
  background-color: #f5f5f5;
  padding: 1rem;
  border: 1px solid #ccc;
  max-height: 400px; /* Limit the height */
  overflow-y: auto; /* Enable scrolling */
}
</style>