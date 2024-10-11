rule sam_to_bam:
    input:
        adjust_output("aligned/{sample}.sam")
    output:
        adjust_output("aligned/{sample}.bam")
    shell:
        "samtools view -Sb {input} > {output}"

rule sort_bam:
    input:
        adjust_output("aligned/{sample}.bam")
    output:
        adjust_output("aligned/{sample}_sorted.bam")
    shell:
        "samtools sort {input} -o {output}"

rule index_bam:
    input:
        adjust_output("aligned/{sample}_sorted.bam")
    output:
        adjust_output("aligned/{sample}_sorted.bam.bai")
    shell:
        "samtools index {input}"

rule variant_calling:
    input:
        bam=adjust_output("aligned/{sample}_sorted.bam"),
        bai=adjust_output("aligned/{sample}_sorted.bam.bai"),
        reference=config["reference"]
    output:
        adjust_output("variants/{sample}.vcf")
    shell:
        """
        gatk HaplotypeCaller \
            -R {input.reference} \
            -I {input.bam} \
            -O {output}
        """