# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

# Read data from csv file
harris1Data = pd.read_csv("data/HarrisPartI.csv")
harris3Data = pd.read_csv("data/HarrisPartIII.csv")
vandenBergData = pd.read_csv("data/vandenBerg_table2.csv")

# Delete name fields from harris1Data
harris1Data.drop(columns=["Name"], inplace=True)

# Rename columns in VandenBerg dataset to match Harris convention 
vandenBergData.rename(columns={'#NGC': "ID"}, inplace=True)

# Define function to add NGC into vandenBerg star IDs
def addNGC(s):
    return "NGC " + s
vandenBergData["ID"] = vandenBergData["ID"].apply(addNGC)

# Merge datasets for matching star IDs
firstMerge = pd.merge(vandenBergData, harris1Data, on="ID")
secondMerge = pd.merge(firstMerge, harris3Data, on="ID")

secondMerge.to_csv('mergedData.csv', index=False)




