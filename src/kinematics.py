# Import libraries
from math import log10, floor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import csv
from scipy.optimize import curve_fit

# import the csv files
harrisI = np.loadtxt('data/HarrisPartI.csv', delimiter=',', skiprows=1, dtype=object)
harrisIII = np.loadtxt('data/HarrisPartIII.csv', delimiter=',', skiprows=1, dtype=object)

# store each relevant column as a new variable
galactic_longitude = harrisI[:,4].astype(float)
velocity_lsr = harrisIII[:,3] #Includes the NA columns. LSR = Local Standard of Rest.
lsr_indicies = np.where(velocity_lsr != 'NA')[0] #Indices of the velocity_lsr array that are not 'NA'
velocity_lsr = velocity_lsr[lsr_indicies].astype(float) # Filter velocity_lsr array to only have numerical values and convert to float
galactic_longitude = galactic_longitude[lsr_indicies] # Filte galactic_longitude array to only include corresponding values    
galctic_centre_radius = harrisI[lsr_indicies,7].astype(float)
ID = harrisI[lsr_indicies,0]

#1. Plot V_LSR vs. l 
#Won't confirm rotation, but any GCs with motions that significantly deviate from the GCs around them may be potential accreeted ones
#First, define the model sinusoidal function to be fitted: V = a*sin(l) + b*cos(l) + c. Least squares regression. 
def model(galactic_longitude, a, b, c):
    l_rad = np.radians(galactic_longitude)  # convert degrees to radians
    return a*np.sin(l_rad) + b*np.cos(l_rad) + c

#Perform curve fitting using scipy.optimize.curve_fit
#best_parameters, covariance = curve_fit(model function, x_data, y_data). From https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
#best_parameters: Array of best-fit values for the model equation: [a, b, c]
#covariance: Covariance matrix of popt - Used to find standard deviation of a, b and c. 
best_parameters, covariance = curve_fit(model, galactic_longitude, velocity_lsr) #curve_fit(model function, x_data, y_data)

#Residuals and outlier array:
residual = velocity_lsr - model(galactic_longitude, best_parameters[0], best_parameters[1], best_parameters[2]) #Difference between data and model for each point
std_residual  = np.std(residual) 
outlier  = np.abs(residual) > 2 * std_residual #Let outliers be any point more than 2 standard deviations from model. 
#^Gives array of true and falses for each GC - True = Outlier

# plot
l_values = np.linspace(0, 360, 361) #Array of degrees from 0 - 360. 
curve  = model(l_values, best_parameters[0], best_parameters[1], best_parameters[2]) # a = best_parameters[0], etc. 

plt.scatter(galactic_longitude[~outlier], velocity_lsr[~outlier], marker ='*', s = 50, label = 'Within 2std', color = 'blue')
#The points with a true index from outlier will be plotted. ~ flips array, so all trues become falses and vice versa. So plot all the falses (non-outliers) first .
plt.scatter(galactic_longitude[outlier], velocity_lsr[outlier], marker ='*', s = 90, color = 'red', label='Outliers (>2std)')
#Plot GCs with true index, which are the outliers. 
plt.plot(l_values, curve, 'k-', label = 'Curve of Best Fit') #Add the sine curve of best fit as a black line
plt.fill_between(l_values, curve - 2*std_residual, curve + 2*std_residual, alpha = 0.3) 
#Colour the region within 2 std of the curve: plt.fill_between(x values, y lower bound, y upper bound). Alpha sets the transperency so the points are all visible. 

#Label outliers with their ID on graph:
for i in np.where(outlier)[0]: #Find where outlier array is true
    plt.annotate(ID[i], (galactic_longitude[i], velocity_lsr[i])) 
    #plt.annotate(Text, (x coordinate, y coordinate))

plt.xlabel('Galactic Longitude (deg)')
plt.ylabel('Velocity (LSR) (km/s)')
plt.title('Velocity_LSR vs. Galactic Longitude') # Title of graph
plt.legend()
plt.show()
print(ID[outlier])
#NEXT: Add spatial plots from paper and identify the outliers from the above graph on those spatial plots to confirm if they are actually accreted. 