import subprocess

def run_variant_calling(ref_genome, target_genome, folder):
    # conda run -n snakemake snakemake --config ref=./data/genome.fa target=./data/A.fastq --cores 1
    # snakemake_cmd = [
    #     "conda", "run", "-n", "snakemake",
    #     "snakemake",
    #     "--config",
    #     f"ref={ref_genome}",
    #     f"target={target_genome}",
    #     f"folder={folder}",
    #     # "--latency-wait", "10",
    #     "-np", #dry run
    #     "--force",
    #     "--cores", "1", f"{target_genome}.vcf"
    # ]

    snakemake_cmd = [
        "conda", "run", "-n", "snakemake", "snakemake",
        "--force", "--dag",
        "--config",
        f"ref={ref_genome}",
        f"target={target_genome}",
        f"folder={folder}"
    ]
    
    try:
        # Run Snakemake with subprocess
        subprocess.run(snakemake_cmd, check=True)
        print("Variant calling workflow executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
# run_variant_calling("data/genome.fa", "data/A.fastq", "/")
# run_variant_calling("maintests/1/genome.fa", "maintests/1/A.fastq", "maintests/1")
run_variant_calling("maintests/3/ecoli_ref.fna", "maintests/3/P0AES4.fasta", "maintests/3")
