from Bio.SeqUtils.ProtParam import ProteinAnalysis
from PyBioMed.PyProtein import AAComposition
from PyBioMed.PyProtein import CTD
import pandas as pd

seq = 'CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKXPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCRECGRGFSDRSSLCYHQRTHTGEKPYVCREDE'
if 'X' in seq:
    seq = seq.replace('X','')

# Analize protein
# res = ProteinAnalysis(seq)

# Extract features
# aac = res.get_amino_acids_percent()    
# molc_weight = res.molecular_weight()
# aromaticity = res.aromaticity()
# instability_index = res.instability_index()
# flexibility = res.flexibility()
# gravy = res.gravy()
# isoelectric_pnt = res.isoelectric_point()
# molar_extinction = res.molar_extinction_coefficient()
# sec_struct = res.secondary_structure_fraction()
# print(molc_weight)
# print(aromaticity)
# print(instability_index)
# print(flexibility)
# print(gravy)
# print(isoelectric_pnt)
# print(molar_extinction)
# print(sec_struct)

# Add all features to dict
# aac['Molc_Weight'] = molc_weight
# aac['Aromaticity'] = aromaticity
# aac['Instability_Index'] = instability_index
# print(aac)

AAC = AAComposition.CalculateAAComposition(seq)
ctd = CTD.CalculateC(seq)
ctd2 = CTD.CalculateCTD(seq)

print(ctd2)

aac_values = []
aac_keys = AAC.keys()
aac_values.append(list(AAC.values()))
df_aac = pd.DataFrame(aac_values, columns=aac_keys)
print(df_aac.head())

ctd_values = []
ctd_keys = ctd.keys()
ctd_values.append(list(ctd.values()))
df_ctd = pd.DataFrame(ctd_values, columns=ctd_keys)
print(df_ctd.head())

res_df = pd.concat([df_aac, df_ctd], axis=1)
# print(res_df.head())