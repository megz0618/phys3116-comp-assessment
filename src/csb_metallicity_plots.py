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

# Map classification labels to colours and display names
categories = {
    "in-situ": ("blue", "In-Situ"),
    "accreted": ("red", "Accreted"),
    "unknown/outlier": ("grey", "Unknown/Outlier")
}

# --- Plotting ---
for classification, (colour, display_name) in categories.items():
    subset = mergeddata[
        mergeddata[classification_column] == classification
    ]
    plt.scatter(
        subset["FeH"],
        subset["r_h"],
        s=30,
        c=colour,
        label=f"{display_name} ({len(subset)} clusters)"
    )

plt.xlabel("Metallicity [Fe/H] (dex)")
plt.ylabel("Half-light Radius $r_h$ (pc)")
plt.title("Metallicity vs Half-light Radius for Milky Way Globular Clusters")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# --- Tables ---
for classification, (_, display_name) in categories.items():
    subset = mergeddata[
        mergeddata[classification_column] == classification
    ]
    print(f"\n=== {display_name} Clusters ({len(subset)} total) ===")
    print(subset[["Harris_Name", classification_column]].to_string(index=False))


#metal rich globular clusters sit lower on the plot meaning that they have brighter cores which is consistsent with Milky Way GCs