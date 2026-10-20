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

# Add colourbar for log_sigma_0 values
sigma0 = plt.scatter(
    vandenBergData["FeH"], vandenBergData["Age"],
    c = vandenBergData["log_sigma_0"], cmap = "viridis", marker = '*', s = 80, zorder = 3
)
plt.colorbar(sigma0, label="Log of Central Density Measure (units)")

plt.legend(loc="lower left")

# Show and save
plt.tight_layout()
# plt.savefig("Age_vs_Metallicity_CDM.png")
plt.show()


