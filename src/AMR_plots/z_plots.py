# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from adjustText import adjust_text

# Plot vandenBerg data with error in age, using separate colours for different methods
# Read data from csv file
vandenBergData = pd.read_csv("data/vandenBerg_table2.csv")

# Plot Metallicity vs Age with errorbars
plt.errorbar(
    vandenBergData["FeH"],
    vandenBergData["Age"],
    yerr = vandenBergData["Age_err"],
    fmt = '*', 
    ecolor = 'gray',
    color = 'lightgray',
    markersize = 6,
    capsize = 2,
)

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label='Linear fit', color = 'orange'
)

# Add colourbar for |Z|
# data = pd.read_csv("data/mergedData.csv")
# vb = data[data["Age"].notna()].copy()
# z = plt.scatter(vb["FeH"], vb["Age"], c = vb["Z"].abs(),
#                 cmap = "viridis", marker = "*", s=80, zorder = 3)
# plt.colorbar(z, label="|Z| (kpc)")

data = pd.read_csv("data/mergedData.csv")
vb = data[data["Age"].notna()].copy() # Isolate just VandenBerg data

# Isolate and label upper and lower outliers from Metallicity-Age relation
accreted = vb[(vb["Age_residual"] < -2) & (vb["Z"].abs() > 3)]
inSitu = vb[(vb["Age_residual"] > 2) & (vb["Z"].abs() <= 3)]
outliers = pd.concat([accreted, inSitu])

for name, x, y in zip(outliers["ID"], outliers["FeH"], outliers["Age"]):
    annot = plt.annotate(name, xy = (x,y), xytext = (5,5), textcoords = "offset points", arrowprops=dict(arrowstyle="->", color="black", lw=0.5))
    annot.draggable(True)

# Add labels and title
plt.xlabel("[Fe/H] (dex)")
plt.ylabel("Age (Gyr)")
plt.title("GC Classifications using Vertical Distance Data \n on Age vs Metallicity Relation")

# Add legend
plt.scatter(accreted["FeH"], accreted["Age"], color="C1", marker="*", s=60, zorder=4, label="Possibly accreted")
plt.scatter(inSitu["FeH"], inSitu["Age"], color="C0", marker="*", s=60, zorder=4, label="Possibly in-situ")
plt.legend(loc="lower left")

# Show and save
plt.tight_layout()
# plt.savefig("Age_vs_Metallicity_Vertical_Distance.png")
plt.show()

# # Add classifications as Classification_Z to mergedData.csv
# for i in range(len(data)):
#     ID = data.loc[i, "ID"]
#     residual = data.loc[i, "Age_residual"]
#     if(pd.isna(residual)): # No age data available
#         data.loc[i, "Classification_Z"] = "No age data"
#     elif(ID in inSitu["ID"].values):
#         data.loc[i, "Classification_Z"] = "In-situ"
#     elif(ID in accreted["ID"].values):
#         data.loc[i, "Classification_Z"] = "Accreted"
#     else:
#         data.loc[i, "Classification_Z"] = "Unresolved"

# # Save predicted classifications to merged csv
# data.to_csv('data/mergedData.csv', index = False)


