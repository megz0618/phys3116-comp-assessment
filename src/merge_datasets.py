# Run this file from phys3116-comp-assessment directory
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Helper functions
# Used to add 'NGC' into VandenBerg star 'ID' field
def addNGC(s):
    return "NGC " + s

# Used to delete spaces in Harris1 dataset 'Name' field
def deleteSpaces(c):
    return c.replace(' ', '')

# Read data from csv file
harris1Data = pd.read_csv("data/HarrisPartI.csv")
harris3Data = pd.read_csv("data/HarrisPartIII.csv")
vandenBergData = pd.read_csv("data/vandenBergClassifications.csv")

# Rename columns in VandenBerg dataset to match Harris convention 
vandenBergData.rename(columns={'#NGC': "ID"}, inplace=True)

# Add 'NGC' into VandenBerg star 'ID' field
for i in range(len(vandenBergData)):
    ID = vandenBergData.loc[i, "ID"]
    if (ID != "XXXX"):
        vandenBergData.loc[i, "ID"] = addNGC(ID)
    else:     
        name = vandenBergData.loc[i, "Name"]
        if (name == "Ter8"):
            name = "Terzan8"
            ID = "Terzan 8"
        elif (name == "Arp21"):
            ID = "Arp 21"
        elif (name == "Pal12"):
            ID = "Pal 12"
        vandenBergData.loc[i, "Name"] = name
        vandenBergData.loc[i, "ID"] = ID

# Delete spaces in Harris1 'Name' field
for j in range(len(harris1Data)):
    name = harris1Data.loc[j, "Name"]
    if (pd.notna(name)):
        harris1Data.loc[j, "Name"] = deleteSpaces(name)

# Rename Vandenberg and Harris' 'Name' fields
vandenBergData.rename(columns={'Name': 'VandenBerg_Name'}, inplace=True)
harris1Data.rename(columns={'Name': 'Harris_Name'}, inplace=True)

# Merge datasets for matching star IDs
# How = left keeps the bigger Harris set, and adds VandenBerg info in 
firstMerge = pd.merge(harris1Data, harris3Data, on = "ID", how = "left")
secondMerge = pd.merge(firstMerge, vandenBergData, on = "ID", how = "left")
secondMerge.to_csv('data/mergedData.csv', index = False)