# This file ensures clusters with no age data aren't labelled as unresolved
# Run this file from phys3116-comp-assessment directory
import pandas as pd

# Read data from csv file
data = pd.read_csv("data/mergedData.csv")
vb = data[data["Age"].notna()].copy() # Isolate just VandenBerg data

# Edit Classifications_AMR based on availability of age data
for i in range(len(data)):
    residual = data.loc[i, "Age_residual"]
    if(pd.isna(residual)): # No age data available
        data.loc[i, "Classification_AMR"] = "No age data"
    elif(residual < -2):
        data.loc[i, "Classification_AMR"] = "Accreted"
    elif(residual > 2):
            data.loc[i, "Classification_AMR"] = "In-situ"
    else:
        data.loc[i, "Classification_AMR"] = "Unresolved"

# Edit Classification_HBType based on availability of age data
s = vb[(vb["FeH"] > -1.5) & (vb["FeH"] < -1.0)] # Isolate region between -1.5 and -1.0 metallicity (where branching is clearest)
accreted = s[(s["Age_residual"] < -2)]
inSitu = s[(s["Age_residual"] > 2)]
for i in range(len(data)):
    ID = data.loc[i, "ID"]
    residual = data.loc[i, "Age_residual"]
    if(pd.isna(residual)): # No age data available
        data.loc[i, "Classification_HBType"] = "No age data"
    elif(ID in inSitu["ID"].values):
        data.loc[i, "Classification_HBType"] = "In-situ"
    elif(ID in accreted["ID"].values):
        data.loc[i, "Classification_HBType"] = "Accreted"
    else:
        data.loc[i, "Classification_HBType"] = "Unresolved"

# Edit Classification_GCR based on availability of age data
accreted = vb[(vb["Age_residual"] < -2) & (vb["R_G"].abs() > 10)]
inSitu = vb[(vb["Age_residual"] > 2) & (vb["R_G"].abs() <= 10)]
for i in range(len(data)):
    ID = data.loc[i, "ID"]
    residual = data.loc[i, "Age_residual"]
    if(pd.isna(residual)): # No age data available
        data.loc[i, "Classification_GCR"] = "No age data"
    elif(ID in inSitu["ID"].values):
        data.loc[i, "Classification_GCR"] = "In-situ"
    elif(ID in accreted["ID"].values):
        data.loc[i, "Classification_GCR"] = "Accreted"
    else:
        data.loc[i, "Classification_GCR"] = "Unresolved"

# Edit Classification_Z based on availability of age data
accreted = vb[(vb["Age_residual"] < -2) & (vb["Z"].abs() > 3)]
inSitu = vb[(vb["Age_residual"] > 2) & (vb["Z"].abs() <= 3)]
for i in range(len(data)):
    ID = data.loc[i, "ID"]
    residual = data.loc[i, "Age_residual"]
    if(pd.isna(residual)): # No age data available
        data.loc[i, "Classification_Z"] = "No age data"
    elif(ID in inSitu["ID"].values):
        data.loc[i, "Classification_Z"] = "In-situ"
    elif(ID in accreted["ID"].values):
        data.loc[i, "Classification_Z"] = "Accreted"
    else:
        data.loc[i, "Classification_Z"] = "Unresolved"

# Save predicted classifications to merged csv
data.to_csv('data/mergedData.csv', index = False)
