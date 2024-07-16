rule sam_to_bam:
    input:
        "{output_dir}/aligned/{sample}.sam"
    output:
        "{output_dir}/aligned/{sample}.bam"
    shell:
        "samtools view -Sb {input} > {output}"

rule sort_bam:
    input:
        "{output_dir}/aligned/{sample}.bam"
    output:
        "{output_dir}/aligned/{sample}_sorted.bam"
    shell:
        "samtools sort {input} -o {output}"

rule index_bam:
    input:
        "{output_dir}/aligned/{sample}_sorted.bam"
    output:
        "{output_dir}/aligned/{sample}_sorted.bam.bai"
    shell:
        "samtools index {input}"

rule variant_calling:
    input:
        bam="{output_dir}/aligned/{sample}_sorted.bam",
        bai="{output_dir}/aligned/{sample}_sorted.bam.bai",
        reference=config["reference"]
    output:
        "{output_dir}/variants/{sample}.vcf"
    shell:
        """
        gatk HaplotypeCaller \
            -R {input.reference} \
            -I {input.bam} \
            -O {output}
        """