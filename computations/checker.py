import pandas as pd
import pysam
from pysam import VariantFile

OMGenes_VCF = VariantFile("Delta.fa.vcf")
Coronapp_csv = pd.read_csv("Delta_Coronapp.csv", sep=",")

OMGenes_ref_pos = []
OMGenes_ref = []
OMGenes_alt = []

for rec in OMGenes_VCF.fetch():
    OMGenes_ref_pos.append(rec.pos)
    OMGenes_ref.append(rec.ref)
    OMGenes_alt.append(rec.alts[0])


OMGenes_pd = pd.DataFrame([OMGenes_ref_pos, OMGenes_ref, OMGenes_alt]).transpose()

OMGenes_pd.rename(columns={0: 'refpos', 1: 'refvar', 2: 'qvar'}, inplace=True)

Coronapp_pd = Coronapp_csv[["refpos", "refvar", "qvar"]]
# print(Coronapp_csv)

merged_dataframe = pd.merge(Coronapp_pd, OMGenes_pd, on='refpos', suffixes=('_coronapp', '_omgenes'), how='left').fillna("NONE")

print(merged_dataframe)

ref_corona = merged_dataframe["refvar_coronapp"]
ref_omgenes = merged_dataframe["refvar_omgenes"]
alt_corona = merged_dataframe["qvar_coronapp"]
alt_omgenes = merged_dataframe["qvar_omgenes"]

TP = len(merged_dataframe[(ref_corona == ref_omgenes) & (alt_corona == alt_omgenes)])

FP = len(merged_dataframe[
    (
        (
            (ref_corona != ref_omgenes) & (ref_omgenes != "NONE")
        )
        |
        (
            (alt_corona != alt_omgenes) & (alt_omgenes != "NONE")
        )
    )
    |
    ((ref_corona == "NONE") & (alt_corona == "NONE"))
    ])
FN = len(merged_dataframe[("NONE" == ref_omgenes) & ("NONE" == alt_omgenes)])
TN = 0

Recall = TP/(TP+FN)
Precision = TP/(TP+FP)
F1_Value = 2 * Precision * Recall / (Precision + Recall)

Sensitivity = TP/(TP+FN)
# Specificity = TN/(TN+FP)

print(f"True Positives:  {TP}")
print(f"False Positives: {FP}")
print(f"False Negatives  {FN}")
print(f"True Negatives:  {TN}")
print("=======================")
print(f"Recall:          {Recall}")
print(f"Precision:       {Precision}")
print(f"F1_Value:        {F1_Value}")
print(f"Sensitivity:     {Sensitivity}")
# print(f"Specificity:     {Specificity}")
