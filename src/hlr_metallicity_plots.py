
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read merged data
mergeddata = pd.read_csv("data/mergedData.csv")

# Clean column names
mergeddata.columns = mergeddata.columns.str.strip()

classification_column = "Classification"

# Clean classification labels
mergeddata[classification_column] = (
    mergeddata[classification_column]
    .fillna("Unknown/Outlier")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Plotting
colours = {
    "in-situ": "blue",
    "accreted": "red",
    "unknown/outlier": "grey"
}

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

# Tables
classification_column = "Classification"
mergeddata[classification_column] = (
    mergeddata[classification_column]
    .fillna("Unknown/Outlier")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Table with Name and Classification
table = mergeddata[["ID", classification_column]]

# Print first 20 rows as a preview
print(table.head(20))

# Table printed
print(table.to_string(index=False))
