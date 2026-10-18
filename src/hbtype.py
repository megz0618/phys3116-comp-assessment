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
    fmt = 'none', 
    ecolor = 'gray',
    markersize = 6,
    capsize = 2,
)

# Fit a linear curve then plot
result = stats.linregress(vandenBergData["FeH"], vandenBergData["Age"])
plt.plot(
    vandenBergData["FeH"], result.slope * vandenBergData["FeH"] + result.intercept,
    label=f'y = {result.slope:.2f} * x + {result.intercept:.2f}'
)

# Add colourbar for HBType values 
hbtype = plt.scatter(
    vandenBergData["FeH"], vandenBergData["Age"],
    c = vandenBergData["HBtype"], cmap = "RdBu", marker = '*', s = 80, zorder = 3
)
plt.colorbar(hbtype, label="HB type")

# Add labels and title
plt.xlabel("FeH (dex)")
plt.ylabel("Age (Gyr)")
plt.title("Metallicity vs Age Relation with HBType for Globular Clusters in the Milky Way")

# Add legend
plt.legend()

# Show and save
plt.show()
plt.savefig("Age_vs_Metallicity_Plot_5.png")