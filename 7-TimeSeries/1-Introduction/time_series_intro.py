# Importing required libraries and functions
import os
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from utils import load_data

# Loading the data
data_dir = '../data'
energy = load_data(data_dir)
print(energy.head())

# Plotting the full energy load dataset
energy.plot(y='load', subplots=True, figsize=(15,8), fontsize=12)
plt.xlabel('timestamp', fontsize=12)
plt.ylabel('load', fontsize=12)
plt.show()

# Plotting one week of energy load data - first week of July 2014
energy['2014-07-01':'2014-07-07'].plot(y='load', subplots=True, figsize=(15, 8), fontsize=12)
plt.xlabel('timestamp', fontsize=12)
plt.ylabel('load', fontsize=12)
plt.show()