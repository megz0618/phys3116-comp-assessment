# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read merged data
mergeddata = pd.read_csv("data/mergedData.csv")

# Scatter plot of metallicity vs half-light radius
plt.scatter(
    mergeddata["FeH"],
    mergeddata["r_h"],
    s=30,
    c='black',
    label="Globular Clusters"
)

# Labels, title, grid
plt.xlabel("Metallicity [Fe/H] (dex)")
plt.ylabel("Half-light Radius r_h (pc)")
plt.title("Metallicity vs Half-light Radius for Milky Way Globular Clusters")
plt.grid(alpha=0.3)
plt.legend()

plt.show()


