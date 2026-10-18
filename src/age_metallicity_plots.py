# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

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

# Add labels and title
plt.xlabel("FeH (dex)")
plt.ylabel("Age (Gyr)")
plt.title("Metallicity vs Age Relation for Globular Clusters in the Milky Way")
#plt.savefig("Age_vs_Metallicity_Plot_1.png")
plt.show()

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
print(result)
print(f'Line has equation y = ...({result.slope:.2f} +- {result.stderr:.2f}) * x + ({result.intercept:.2f} +- {result.intercept_stderr:.2f})')
print(f'Result has R-value of {result.rvalue:.2f} and p-value of {result.pvalue:.2e}')

plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label=f'y = {result.slope:.2f} * x + {result.intercept:.2f}'
)

# Add legend, then save plot
plt.legend()
#plt.savefig("Age_vs_Metallicity_Plot_2.png")
plt.show()

# Plot normlaised residuals for each cluster
vandenBergData["Age_residual"] = (vandenBergData["Age"] - (result.slope * vandenBergData["FeH"] + result.intercept)) / vandenBergData["Age_err"]
plt.scatter(vandenBergData["FeH"], vandenBergData["Age_residual"])
plt.xlabel("[Fe/H] (dex)")
plt.ylabel(r"Normalised Age Residual ($\sigma$)")
plt.title("Residuals in Linear Fit of Metallicity vs Age Relation")
#plt.savefig("Age_vs_Metallicity_Plot_3.png")
plt.show()

# Identify accreted and in-situ globular clusters based on residual
for i in range(len(vandenBergData)):
    sigma = vandenBergData.loc[i, "Age_residual"]
    if((sigma > 2)):
        vandenBergData.loc[i, "Classification"] = "In-situ"
    elif(sigma < -2):
        vandenBergData.loc[i, "Classification"] = "Accreted"
    else:
        vandenBergData.loc[i, "Classification"] = "Unresolved"

# Plot residuals in colour bands
inSitu = vandenBergData[(vandenBergData["Classification"] == 'In-situ')]
accreted = vandenBergData[(vandenBergData["Classification"] == 'Accreted')]
unresolved = vandenBergData[(vandenBergData["Classification"] == 'Unresolved')]

plt.scatter(
    inSitu["FeH"], inSitu["Age_residual"],
    label='In situ'
)

plt.scatter(
    accreted["FeH"], accreted["Age_residual"],
    label='Accreted'
)

plt.scatter(
    unresolved["FeH"], unresolved["Age_residual"],
    label='Unresolved'
)

plt.xlabel("[Fe/H] (dex)")
plt.ylabel(r"Normalised Age Residual ($\sigma$)")
plt.title("Grouped Residuals in Linear Fit of Metallicity vs Age Relation")
plt.legend(loc="lower left")
#plt.savefig("Age_vs_Metallicity_Plot_4.png")
plt.show()

# Save predicted classifications to csv
vandenBergData.to_csv('data/vandenBergClassifications.csv', index = False)
