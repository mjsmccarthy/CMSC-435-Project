import pandas as pd
from PyBioMed.PyProtein import AAComposition
from PyBioMed.PyProtein import CTD
from pandas_ml import ConfusionMatrix

'''Generates features for the training dataset'''
def generate_features(df):
    aac_keys = []
    aac_values = []
    ctd_keys = []
    ctd_values = []

    for row in df.itertuples(index=False):
        my_seq = row[0].replace('X', '')
        my_seq = my_seq.replace('Z', '')
        aac = AAComposition.CalculateAAComposition(my_seq)
        ctd = CTD.CalculateC(my_seq)
        aac_keys = aac.keys()
        aac_values.append(list(aac.values()))
        ctd_keys = ctd.keys()
        ctd_values.append(list(ctd.values()))

    # Create dataframes
    df_aac = pd.DataFrame(aac_values, columns=aac_keys)
    df_ctd = pd.DataFrame(ctd_values, columns=ctd_keys)
    # Concat dataframes into single dataframe
    res_df = pd.concat([df_aac, df_ctd], axis=1)
    res_df = pd.concat([df, res_df], axis=1)
    # Send dataframe to csv
    res_df.to_csv('generated_features.csv', index=False)

'''Generates a confusion matrix from predicted values for a given model and outputs statistics.'''
def generate_cm_stats(df):
    y_true = list(df['Label'])
    y_pred = list(df['prediction(Label)'])
    confusion_matrix = ConfusionMatrix(y_true, y_pred)
    confusion_matrix.print_stats()

if __name__ == '__main__':
    # Import datasets
    df_features = pd.read_csv("training_dataset.csv", names=['Sequence', 'Label'])
    df_predicted = pd.read_csv("predicted_features.csv")

    generate_features(df_features)
    generate_cm_stats(df_predicted)
