rule fastqc:
    input:
        adjust_input("{sample}")
    output:
        adjust_output("qc/{sample}_fastqc.html")
    shell:
        "fastqc {input} -o {wildcards.output_dir}/qc/"