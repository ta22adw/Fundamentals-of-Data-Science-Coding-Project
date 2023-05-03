#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:09:31 2023

@author: timothyatoyebi 22027370
"""

# Fundamentals of Data Science By 22027370
# Assignment : Coding project
# Github : https://github.com/ta22adw/Fundamentals-of-Data-Science-Coding-Project

# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Importing the csv file
dataf = pd.read_csv('data0.csv', header=None)
dataf.columns = ['Weight']
print(dataf)

# Create a histogram of newborn weights
plt.hist(dataf, bins='auto', edgecolor='black', label='Newborn Weights')
plt.xlabel('Newborn Weight (Kg)')
plt.ylabel('Frequency')
plt.rcParams["figure.dpi"] = 300

# calculating the average weight of newborns (W̃)
A_weight = np.mean(dataf['Weight'])
print('Average Weight = ' +  str(A_weight))

# calculating X such that 75% of newborns are above (X)
X = np.percentile(dataf['Weight'], 25)
print('Newborns weight above X = ' + str(X))

# Adding the title
plt.title('Distribution of Newborn Weights')

# Adding W̃ and X values to the graph
plt.axvline(A_weight, color='y', linestyle='dashed', linewidth=1, \
            label=f'Average weight (W̃) = {A_weight:.2f} Kg')
plt.axvline(X, color='m', linestyle='dashed', \
            linewidth=1, label=f'25th percentile (X) = {X:.2f} Kg')

# Adding the legend
plt.legend()

# showing the plot
plt.show()