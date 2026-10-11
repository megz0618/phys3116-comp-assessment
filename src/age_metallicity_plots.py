
# Run this file from phys3116-comp-assessment directory
import matplotlib.pyplot as plt
import pandas as pd

krauseData = pd.read_csv("data/Krause21.csv")
plt.scatter(krauseData["Age"], krauseData["FeH"])
plt.ylabel("FeH (units)")
plt.xlabel("Age (units)")
plt.title("Krause21 Age vs Metallicity Plot")
plt.show()

# next step: include error 
vandenBergData = pd.read_csv("data/vandenBerg_table2.csv")
plt.scatter(vandenBergData["Age"], vandenBergData["FeH"])
plt.ylabel("FeH (units)")
plt.xlabel("Age (units)")
plt.title("VandenBerg Age vs Metallicity Plot")
plt.show()

