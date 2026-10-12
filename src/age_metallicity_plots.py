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
plt.title("Linearly Fitted Metallicity vs Age Relation for Globular Clusters in the Milky Way")
# plt.savefig("Age_vs_Metallicity_Plot_1.png")
# plt.show()

# Label and exclude outlier from linear fitting
vandenBergOutlier = vandenBergData[vandenBergData["Name"] == "Pal12"]
plt.annotate(
    "Pal12",
    (vandenBergOutlier["FeH"].iloc[0], vandenBergOutlier["Age"].iloc[0]),
    xytext = (10,0),
    textcoords="offset points",
)
vandenBergNoOutlier = vandenBergData[vandenBergData["Name"] != "Pal12"]

# Fit a linear curve, then plot
result = stats.linregress(vandenBergNoOutlier["FeH"], vandenBergNoOutlier["Age"])
print(result)
print(f'Line has equation y = ...({result.slope:.2f} +- {result.stderr:.2f}) * x + ({result.intercept:.2f} +- {result.intercept_stderr:.2f})')
print(f'Result has R-value of {result.rvalue:.2f} and p-value of {result.pvalue:.2e}')

plt.plot(
    vandenBergNoOutlier["FeH"], result.slope * vandenBergNoOutlier["FeH"] + result.intercept,
    label=f'y = {result.slope:.2f} * x + {result.intercept:.2f}'
)

# Add legend, then save plot
plt.legend()
# plt.savefig("Age_vs_Metallicity_Plot_2.png")
# plt.show()

# Plot standardised residuals
standardisedAgeResiduals = (vandenBergNoOutlier["Age"] - (result.slope * vandenBergNoOutlier["FeH"] + result.intercept)) / vandenBergNoOutlier["Age_err"]
plt.scatter(vandenBergNoOutlier["FeH"], standardisedAgeResiduals)
plt.xlabel("[Fe/H] (dex)")
plt.ylabel("Age Residuals (Gyr)")
plt.title("Residuals in Linear Fit of Metallicity vs Age Relation")
# plt.savefig("Age_vs_Metallicity_Plot_3.png")
# plt.show()

