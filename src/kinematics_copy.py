# Import libraries
from math import log10, floor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import csv
import pandas as pd

# import the csv files
mergedData = pd.read_csv("data/mergedData.csv")
cleanedData = mergedData.dropna(subset=["L"])

inSitu = cleanedData[(cleanedData["Classification"] == 'In-situ')]
accreted = cleanedData[(cleanedData["Classification"] == 'Accreted')]
unresolved = cleanedData[(cleanedData["Classification"] == 'Unresolved')]

plt.scatter(
    inSitu["L"], inSitu["v_LSR"],
    label='In situ'
)

plt.scatter(
    accreted["L"], accreted["v_LSR"],
    label='Accreted'
)

plt.scatter(
    unresolved["L"], unresolved["v_LSR"],
    label='Unresolved'
)

plt.xlabel('Galactic Longitude (deg)') # x-axis label
plt.ylabel('Velocity (LSR) (km/s)') # y-axis label
plt.title('Velocity_LSR vs. Galactic Longitude') # Title of graph
plt.legend(loc="upper left")
plt.show()