<template>
  <div>
    <v-card title="Snakemake Workflow" class="pa-4 w-100">
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

    <v-card-text>
        Above is the Snakemake workflow used to create the VCF Files from a reference and sample genome. It makes use of a simple alignment-based process to create VCF files. <br><br>
        This workflow is run in a Conda Environment with BWA, BCFTools, and Samtools which has various tools needed in the different steps of the Variant Call. <br><br>
        The variant call is done through "rules" done in the order that you see above, and a simple explanation of the process is below:<br>
        1. Index files for the reference genomes are created using BWA<br>
        2. Using the created index files, the sample genome is then mapped to the reference genome using BWA and Samtools<br>
        3. The map of the sample genome is then sorted using Samtools<br>
        4. The sorted map of the sample genome is then indexed using Samtools<br>
        5. Finally, using the sorted map of the sample genome and the reference genome, BCFTools then runs the final Variant Call<br>
        <br>
        This workflow was based off the Tutorial Workflow from Snakemake but adjusted to add the indexing for the reference genome and dynamicity of files.
    </v-card-text>
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