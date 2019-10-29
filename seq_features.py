import pandas as pd
import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis

df = pd.read_csv("training_dataset.csv", names=['Sequence', 'Label'])
print(df.head(20))
print(df.shape)

cols = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'Molec_Weight']
lst = []

for row in df.itertuples(index=False):
    my_seq = row[0].replace('X', '')
    my_seq = my_seq.replace('Z', '')
    analysed_seq = ProteinAnalysis(my_seq)
    freq = analysed_seq.get_amino_acids_percent()
    molc_weight = analysed_seq.molecular_weight()
    for k, v in freq.items():
        freq[k] = round(v, 4)
    freq['Molc_Weight'] = molc_weight
    lst.append(list(freq.values()))

df2 = pd.DataFrame(lst, columns=cols)
res_df = pd.concat([df, df2], axis=1)

res_df.to_csv('features.csv', index=False)