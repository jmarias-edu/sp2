rule fastqc:
    input:
        "data/samples/{sample}_R1.fastq",
        "data/samples/{sample}_R2.fastq"
    output:
        "{output_dir}/qc/{sample}_R1_fastqc.html",
        "{output_dir}/qc/{sample}_R2_fastqc.html"
    shell:
        "fastqc {input} -o {wildcards.output_dir}/qc/"