# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

# Plot vandenBerg data with error in age, using separate colours for different methods
# Read data from csv file
vandenBergData = pd.read_csv("data/vandenBerg_table2.csv")

# Separate based on method used for data extraction
vertical = vandenBergData[(vandenBergData["Method"] == 'V')]
horizontal = vandenBergData[(vandenBergData["Method"] == 'H')]
average = vandenBergData[(vandenBergData["Method"] == 'A')]

# Plot each method's data separately, with errorbars
plt.errorbar(
    vertical["FeH"],
    vertical["Age"],
    yerr = vertical["Age_err"],
    fmt = 'o', 
    ecolor = 'gray',
    markersize = 4,
    capsize = 2,
    label = 'Vertical Method'
)

plt.errorbar(
    horizontal["FeH"],
    horizontal["Age"],
    yerr = horizontal["Age_err"],
    fmt = 's', 
    ecolor = 'gray',
    markersize = 4,
    capsize = 2,
    label = 'Horizontal Method'
)

plt.errorbar(
    average["FeH"],
    average["Age"],
    yerr = average["Age_err"],
    fmt = '*', 
    ecolor = 'gray',
    markersize = 6,
    capsize = 2,
    label = 'Average Method'
)

# Add labels and title
plt.xlabel("FeH (dex)")
plt.ylabel("Age (Gyr)")
plt.title("Linearly Fitted Metallicity vs Age Relation for Globular Clusters in the Milky Way")

# Fit a linear curve, then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
print(result)
print(f'Line has equation y = ({result.slope:.2f} +- {result.stderr:.2f}) * x + ({result.intercept:.2f} +- {result.intercept_stderr:.2f})')
print(f'Result has R-value of {result.rvalue:.2f} and p-value of {result.pvalue:.2e}')

plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label=f'y = {result.slope:.2f} * x + {result.intercept:.2f}'
)

# Add legend, then save plot
plt.legend()
plt.savefig("Age_vs_Metallicity_Plot_2.png")
plt.show()

