rule bwa_index:
    input:
        config["reference"]
    output:
        "{reference}.bwt"
    shell:
        "bwa index {input}"

rule bwa_mem:
    input:
        reference=config["reference"],
        r1="data/samples/{sample}_R1.fastq",
        r2="data/samples/{sample}_R2.fastq"
    output:
        "{output_dir}/aligned/{sample}.sam"
    shell:
        "bwa mem {input.reference} {input.r1} {input.r2} > {output}"