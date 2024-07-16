rule bwa_mem:
    input:
        reference=config["reference"],
        read=adjust_input("{sample}")
    output:
        adjust_output("aligned/{sample}.sam")
    shell:
        "bwa mem {input.reference} {input.read} > {output}"