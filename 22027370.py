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
weights = []
with open('data0.csv') as file:
    dataf = pd.read_csv(file)
    for row in dataf:
        weights.append(float(row[0]))
print(dataf)

# calculating the average weight of newborns (˜W )
average_weight = np.mean(weights)
w = average_weight
print(w)


# calculating X such that 75% of newborns are above (X)
X = np.percentile(weights, 25)

# ploting histogram of the weights distribution
plt.hist(weights, bins=20)
plt.rcParams["figure.dpi"] = 300

# Adding w and X values to the graph
plt.axvline(w, color='b', linestyle='dashed', linewidth=10)
plt.axvline(X, color='r', linestyle='dashed', linewidth=5)

# Adding the labels
plt.xlabel('Newborns Weight (kg)')
plt.ylabel('Frequency')

# Adding the title
plt.title('Distribution of Newborn Weights')

# Adding the legend
plt.legend(['Mean weight: {:.2f} kg'.format(w), 'X: {:.2f} kg'.format(X)])

# showing the plot
plt.show()