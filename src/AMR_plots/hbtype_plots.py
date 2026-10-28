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
plt.errorbar(vandenBergData["FeH"], vandenBergData["Age"], 
             yerr = vandenBergData["Age_err"], fmt = '*', 
              ecolor = 'lightgray', color = 'gray', markersize = 6, capsize = 2
)

# Add colourbar for HBType values 
hbtype = plt.scatter(vandenBergData["FeH"], vandenBergData["Age"],
    c = vandenBergData["HBtype"], cmap = "RdBu", marker = '*', s = 80, zorder = 3)
plt.colorbar(hbtype, label="HB type")

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
plt.plot(vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label='Linear fit', color = 'black'
)

vandenBergData = pd.read_csv("data/mergedData.csv")
# Isolate region between -1.5 and -1.0 metallicity
s = vandenBergData[(vandenBergData["FeH"] > -1.5) & (vandenBergData["FeH"] < -1.0)] 
# Add vertical lines at these thresholds
plt.axvline(x=-1.5, color='black', linestyle='--', linewidth=1)
plt.axvline(x=-1.0, color='black', linestyle='--', linewidth=1)

# Identify accreted and in-situ candidates
median = s["HBtype"].median()
accreted = s[(s["Age_residual"] < -2) & (s["HBtype"] < median)]
inSitu  = s[(s["Age_residual"] > 2) & (s["HBtype"] > median)]

# Add labels and title
plt.xlabel("[Fe/H] (dex)")
plt.ylabel("Age (Gyr)")
plt.title("GC Classifications using HB Type Data \n on Age vs Metallicity Relation")

# Add legend
plt.scatter(accreted["FeH"], accreted["Age"], color="C4", 
            marker="*", s=60, zorder=4, label="Possibly accreted")
plt.scatter(inSitu["FeH"], inSitu["Age"], color="C2", 
            marker="*", s=60, zorder=4, label="Possibly in-situ")
plt.legend(loc="lower left")

outliers = pd.concat([accreted, inSitu])
for name, x, y in zip(outliers["ID"], outliers["FeH"], outliers["Age"]):
    annot = plt.annotate(name, xy = (x,y), xytext = (5,5), textcoords = "offset points", arrowprops=dict(arrowstyle="->", color="black", lw=0.5))
    annot.draggable(True)

# Show and save
plt.tight_layout()
# plt.savefig("Age_vs_Metallicity_HBType.png")
plt.show()

# data = pd.read_csv("data/mergedData.csv")
# # Add classifications as Classification_HBType to mergedData.csv
# for i in range(len(data)):
#     ID = data.loc[i, "ID"]
#     residual = data.loc[i, "Age_residual"]
#     if(pd.isna(residual)): # No age data available
#         data.loc[i, "Classification_HBType"] = "No age data"
#     elif(ID in inSitu["ID"].values):
#         data.loc[i, "Classification_HBType"] = "In-situ"
#     elif(ID in accreted["ID"].values):
#         data.loc[i, "Classification_HBType"] = "Accreted"
#     else:
#         data.loc[i, "Classification_HBType"] = "Unresolved"

# # Save predicted classifications to merged csv
# data.to_csv('data/mergedData.csv', index = False)


