# CMSC-435-Project

# Prerequsites 
Python version: 2.7

Python Packages:
- Pandas
- PyBioMed: https://github.com/gadsbyfly/PyBioMed 
    - The prerequisites listed on the repo are not required. You can just download the PyBioMed package and it will work.


# Description
Using the training_dataset.csv file, the python script generates a generated_features.csv file based on each protein sequence. These generated features can then be used in RapidMiner to create a predictive model

`Note:` Additional features can be added with the use of the PyBioMed package.


# Resources
Add resource links here

Operator toolbox has bootstrap upsampling
https://marketplace.rapidminer.com/UpdateServer/faces/product_details.xhtml?productId=rmx_operator_toolbox
To add extention just open RapidMiner -> Extentions -> Marketplace -> search "smote" -> install operator toolbox
SMOTE upsampling will be under operator after rebooting rapidminer

# Using Calculate_Stats.xlsx
Copy confusion matrix from RapidMiner "Results" tab
Paste into empty cells on exel sheet
Copy the cells you just pasted again
Go to Edit-> Paste Special -> Check option for "Transpose" -> Click OK
Paste the transposed matrix into "Actual" cells
Table below "Actual" should update with calculations
