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
    markersize = 6,
    capsize = 2,
)

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label='Linear fit', color = 'orange'
)

# Add colourbar for HBType values 
# hbtype = plt.scatter(
#     vandenBergData["FeH"], vandenBergData["Age"],
#     c = vandenBergData["HBtype"], cmap = "RdBu", marker = '*', s = 80, zorder = 3
# )
# plt.colorbar(hbtype, label="HB type")

# Add colourbar for R_G values 
# rg = plt.scatter(
#    vandenBergData["FeH"], vandenBergData["Age"],
#    c = vandenBergData["R_G"], cmap = "viridis", marker = '*', s = 80, zorder = 3
# )
# plt.colorbar(rg, label="Galactocentric Radius (kpc)")

# Add colourbar for log_sigma_0 values
# sigma0 = plt.scatter(
#     vandenBergData["FeH"], vandenBergData["Age"],
#     c = vandenBergData["log_sigma_0"], cmap = "viridis", marker = '*', s = 80, zorder = 3
# )
# plt.colorbar(sigma0, label="Log of Central Density Measure (units)")

# Add colourbar for |Z|
# data = pd.read_csv("data/mergedData.csv")
# vb = data[data["Age"].notna()].copy()
# z = plt.scatter(vb["FeH"], vb["Age"], c = vb["Z"].abs(),
#                 cmap = "viridis", marker = "*", s=80, zorder = 3)
# plt.colorbar(z, label="|Z| (kpc)")

data = pd.read_csv("data/mergedData.csv")
vb = data[data["Age"].notna()].copy() # Isolate just VandenBerg data

# s = vb[(vb["FeH"] > -1.5) & (vb["FeH"] < -1.0)] # Isolate region between -1.5 and -1.0 metallicity (where branching is clearest)
# # Add vertical lines at these thresholds
# plt.axvline(x=-1.5, color='black', linestyle='--', linewidth=1, label='[Fe/H] = -1.5 (dex)')
# plt.axvline(x=-1.0, color='black', linestyle='--', linewidth=1, label='[Fe/H] = -1.0 (dex)')

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
plt.title("GC Classifications using Age vs Metallicity Relation \n and Vertical Distance Data")

# # Add legend
plt.scatter(accreted["FeH"], accreted["Age"], color="orange", marker="*", s=60, zorder=4, label="Possibly accreted")
plt.scatter(inSitu["FeH"], inSitu["Age"], color="green", marker="*", s=60, zorder=4, label="Possibly in-situ")
plt.legend(loc="lower left")

# Show and save
plt.tight_layout()
# plt.savefig("Age_vs_Metallicity_GCR.png")
plt.show()

# Add classifications as Classification_HBType to mergedData.csv
for i in range(len(data)):
    ID = data.loc[i, "ID"]
    if(ID in inSitu["ID"].values):
        data.loc[i, "Classification_Z"] = "In-situ"
    elif(ID in accreted["ID"].values):
        data.loc[i, "Classification_Z"] = "Accreted"
    else:
        data.loc[i, "Classification_Z"] = "Unresolved"

# Save predicted classifications to merged csv
data.to_csv('data/mergedData.csv', index = False)


