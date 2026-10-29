# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

# Plot vandenBerg data with error in age
# Read data from csv file
# vandenBergData = pd.read_csv("data/vandenBerg_table2.csv")

# # Plot Metallicity vs Age with errorbars
# plt.errorbar(vandenBergData["FeH"], vandenBergData["Age"], 
#              yerr = vandenBergData["Age_err"], fmt = '*', 
#               ecolor = 'gray', markersize = 6, capsize = 2
# )

# # Add labels and title
# plt.xlabel("[Fe/H] (dex)")
# plt.ylabel("Age (Gyr)")
# plt.title("Age vs Metallicity Relation")
# # plt.savefig("Age_vs_Metallicity.png")

# # Fit a linear curve then plot
# result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
# print(result)
# print(f'Line has equation y = ...({result.slope:.2f} +- {result.stderr:.2f}) * x + ({result.intercept:.2f} +- {result.intercept_stderr:.2f})')
# print(f'Result has R-value of {result.rvalue:.2f} and p-value of {result.pvalue:.2e}')

# plt.plot(
#     vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
#     label=f'y = {result.slope:.2f} * x + {result.intercept:.2f}'
# )

# # Add legend, then save plot
# plt.legend()
# # plt.savefig("Age_vs_Metallicity_Linear_Fit.png")
# plt.show()

# # Plot normalised residuals for each cluster
# vandenBergData["Age_residual"] = (vandenBergData["Age"] - (result.slope * vandenBergData["FeH"] + result.intercept)) / vandenBergData["Age_err"]
# plt.scatter(vandenBergData["FeH"], vandenBergData["Age_residual"])
# plt.xlabel("[Fe/H] (dex)")
# plt.ylabel(r"Normalised Age Residual ($\sigma$)")
# plt.title("Residuals in Linear Fit of Age vs Metallicity Relation")
# # plt.savefig("Age_vs_Metallicity_Residuals.png")
# plt.show()

# # Identify accreted and in-situ globular clusters based on residual
# for i in range(len(vandenBergData)):
#     sigma = vandenBergData.loc[i, "Age_residual"]
#     if((sigma > 2)):
#         vandenBergData.loc[i, "Classification"] = "In-situ"
#     elif(sigma < -2):
#         vandenBergData.loc[i, "Classification"] = "Accreted"
#     else:
#         vandenBergData.loc[i, "Classification"] = "Unresolved"

# # Plot residuals in colour bands
# inSitu = vandenBergData[(vandenBergData["Classification"] == 'In-situ')]
# accreted = vandenBergData[(vandenBergData["Classification"] == 'Accreted')]
# unresolved = vandenBergData[(vandenBergData["Classification"] == 'Unresolved')]

# plt.scatter(inSitu["FeH"], inSitu["Age_residual"], label='In situ')
# plt.scatter(accreted["FeH"], accreted["Age_residual"], label='Accreted')
# plt.scatter(unresolved["FeH"], unresolved["Age_residual"], label='Unresolved')

# plt.xlabel("[Fe/H] (dex)")
# plt.ylabel(r"Normalised Age Residual ($\sigma$)")
# plt.title("GC Classifications using Residuals from Linear Fit \n of Age vs Metallicity Relation")
# plt.legend(loc="lower left")
# #plt.savefig("Age_vs_Metallicity_Grouped_Residuals.png")
# plt.show()

# Save predicted classifications to csv
#vandenBergData.to_csv('data/vandenBergClassifications.csv', index = False)

# Reproduce linear fit plot, now coloured using residual classifications
# Allows more direct comparison to Leaman
# Read data from csv file
vandenBergData = pd.read_csv("data/vandenBergClassifications.csv")

# Plot Metallicity vs Age with errorbars
plt.errorbar(
    vandenBergData["FeH"],
    vandenBergData["Age"],
    yerr = vandenBergData["Age_err"],
    fmt = '*', 
    color = 'gray',
    ecolor = 'lightgray',
    markersize = 6,
    capsize = 2,
    label = 'Unresolved'
)

# Add labels and title
plt.xlabel("[Fe/H] (dex)")
plt.ylabel("Age (Gyr)")
plt.title("GC Classifications using Residuals \n on Age vs Metallicity Relation")
# plt.savefig("Age_vs_Metallicity.png")

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label='Linear fit', color = 'C2'
)

# Colour based on classification
inSitu = vandenBergData[(vandenBergData["Classification"] == 'In-situ')]
accreted = vandenBergData[(vandenBergData["Classification"] == 'Accreted')]
unresolved = vandenBergData[(vandenBergData["Classification"] == 'Unresolved')]

plt.scatter(
    inSitu["FeH"], inSitu["Age"],
    label = 'Possibly in situ',
    marker = '*',
    color = 'C0',
    s = 60,
    zorder = 3,
)

plt.scatter(
    accreted["FeH"], accreted["Age"],
    label = 'Possibly accreted',
    marker = '*', 
    color = 'C1',
    s = 60,
    zorder = 3,
)

outliers = pd.concat([accreted, inSitu])
for name, x, y in zip(outliers["#NGC"], outliers["FeH"], outliers["Age"]):
    if (name != 'Pal 12'):
        name = 'NGC ' + str(name)
    annot = plt.annotate(name, xy = (x,y), xytext = (5,5), textcoords = "offset points", arrowprops=dict(arrowstyle="->", color="black", lw=0.5))
    annot.draggable(True)

# Add legend, then save plot
plt.legend(loc='lower left')
# plt.savefig("Age_vs_Metallicity_Linear_Fit.png")
plt.show()