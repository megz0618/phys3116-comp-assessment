#Matched Milky way globular cluster behavior since half light radius correlated more strongly Galactrocentric distance
#Metallicity correlated with cluster population type (halo vs bulge)
#Metallicity does not control structural parameters like r_h

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read merged data
mergeddata = pd.read_csv("data/mergedData.csv")

# Clean column names
mergeddata.columns = mergeddata.columns.str.strip()

# Use the correct classification column name
classification_column = "Classification"

# Clean classification labels
mergeddata[classification_column] = (
    mergeddata[classification_column]
    .fillna("Unknown/Outlier")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Map classification labels to colours
colours = {
    "in-situ": "blue",
    "accreted": "red",
    "unknown/outlier": "grey"
}

# Plot each classification
for classification, colour in colours.items():
    subset = mergeddata[
        mergeddata[classification_column] == classification
    ]
    plt.scatter(
        subset["FeH"],
        subset["r_h"],
        s=30,
        c=colour,
        label=f"{classification.title()} ({len(subset)} clusters)"
    )

plt.xlabel("Metallicity [Fe/H] (dex)")
plt.ylabel("Half-light Radius $r_h$ (pc)")
plt.title("Metallicity vs Half-light Radius for Milky Way Globular Clusters")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Ensure classification column is consistent
classification_column = "Classification"
mergeddata[classification_column] = (
    mergeddata[classification_column]
    .fillna("Unknown/Outlier")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Create a simple table of cluster name + category
table = mergeddata[["Harris_Name", classification_column]]

# Print first 20 rows as a preview
print(table.head(20))

# If you want the whole table printed:
print(table.to_string(index=False))
