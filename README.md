# CMSC-435-Project

# Prerequsites 
Python version: 2.7

Python Packages:
- Pandas
- PyBioMed: https://github.com/gadsbyfly/PyBioMed 
    - The prerequisites listed on the repo are not required. You can just download the PyBioMed package and it will work.
- Pandas-ml: https://pandas-ml.readthedocs.io/en/latest/conf_mat.html#seaborn-plot-of-a-binary-confusion-matrix-todo
    - Install using pip. This package can be used to get stats from a confusion matrix. The link shows an example.


# Description
Using the training_dataset.csv file, the python script does two main things:
1. Generates a features.csv file from training_dataset.csv
2. Prints the statistics for a confusion matrix where a predicted_features.csv file has been provided. The predicted_features.csv should come from the result of our model via RapidMiner. You can export the dataset genreated by the model as a csv file.

We can add or remove features later. This is just a starting point.


# Resources
Add resource links here

Operator toolbox has bootstrap upsampling
https://marketplace.rapidminer.com/UpdateServer/faces/product_details.xhtml?productId=rmx_operator_toolbox
To add extention just open RapidMiner -> Extentions -> Marketplace -> search "smote" -> install operator toolbox
SMOTE upsampling will be under operator after rebooting rapidminer
