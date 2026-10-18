# Import libraries
from math import log10, floor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import csv

# import the csv files
harrisI = np.loadtxt('data/HarrisPartI.csv', delimiter=',', skiprows=1, dtype=object)
harrisIII = np.loadtxt('data/HarrisPartIII.csv', delimiter=',', skiprows=1, dtype=object)

# store each column as a new variable
galactic_longitude = harrisI[:,4].astype(float)
velocity_lsr = harrisIII[:,3] #Includes the NA columns. LSR = Local Standard of Rest.
lsr_indicies = np.where(velocity_lsr != 'NA')[0] #Indices of the velocity_lsr array that are not 'NA'
velocity_lsr = velocity_lsr[lsr_indicies].astype(float) # Filter velocity_lsr array to only have numerical values and convert to float
galactic_longitude = galactic_longitude[lsr_indicies] # Filte galactic_longitude array to only include corresponding values    
galctic_centre_radius = harrisI[lsr_indicies,7].astype(float)

#plt.scatter(galctic_centre_radius, velocity_lsr, marker='*', s=50) <- Without colour bar
l_vlsr_plot = plt.scatter(galactic_longitude, velocity_lsr, c=galctic_centre_radius, cmap='viridis',marker='*', s=50)
plt.colorbar(l_vlsr_plot, label='Galactic Centre Radius (kpc)')
plt.title('Velocity_LSR vs. Galactic Longitude') # Title of graph
plt.xlabel('Galactic Longitude (deg)') # x-axis label
plt.ylabel('Velocity (LSR) (km/s)') # y-axis label
plt.show()

# Plot error bars using the v_r_e column - Do later