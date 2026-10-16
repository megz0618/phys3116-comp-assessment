import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read merged data
mergeddata = pd.read_csv("data/mergedData.csv")

# Scatter plot of central surface brightness vs metallicity
plt.scatter(
    mergeddata["FeH"],
    mergeddata["mu_V"],
    s=30,
    c='black',
    label="Globular Clusters"
)

# Labels, title, grid
plt.xlabel("Metallicity [Fe/H] (dex)")
plt.ylabel("Central Surface Brightness μ_V (mag arcsec$^{-2}$)")
plt.title("Central Surface Brightness vs Metallicity for Milky Way Globular Clusters")
plt.grid(alpha=0.3)
plt.legend()

plt.show()
