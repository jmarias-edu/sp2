import subprocess

def run_variant_calling(ref_genome, target_genome):
    # conda run -n snakemake snakemake --config ref=./data/genome.fa target=./data/A.fastq --cores 1
    snakemake_cmd = [
        "conda", "run", "-n", "snakemake",
        "snakemake", 
        "--config", 
        f"ref={ref_genome}", 
        f"target={target_genome}",
        "--cores", "1", "variants.vcf"
    ]

    # snakemake_cmd = [
    #     # "conda", "run", "-n", "snakemake",
    #     "snakemake", 
    #     "--cores", "1", "variants.vcf"
    # ]
    
    try:
        # Run Snakemake with subprocess
        subprocess.run(snakemake_cmd, check=True)
        print("Variant calling workflow executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
run_variant_calling("data/genome.fa", "data/A.fastq")
