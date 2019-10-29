import pandas as pd
import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from PyBioMed.PyProtein import AAComposition
from PyBioMed.PyProtein import CTD

df_input = pd.read_csv("training_dataset.csv", names=['Sequence', 'Label'])
print(df_input.head(20))
print(df_input.shape)

aac_keys = []
aac_values = []
ctd_keys = []
ctd_values = []

for row in df_input.itertuples(index=False):
    my_seq = row[0].replace('X', '')
    my_seq = my_seq.replace('Z', '')
    aac = AAComposition.CalculateAAComposition(my_seq)
    ctd = CTD.CalculateC(my_seq)
    aac_keys = aac.keys()
    aac_values.append(list(aac.values()))
    ctd_keys = ctd.keys()
    ctd_values.append(list(ctd.values()))

df_aac = pd.DataFrame(aac_values, columns=aac_keys)
df_ctd = pd.DataFrame(ctd_values, columns=ctd_keys)
res_df = pd.concat([df_aac, df_ctd], axis=1)
res_df = pd.concat([df_input, res_df], axis=1)

res_df.to_csv('features2.csv', index=False)