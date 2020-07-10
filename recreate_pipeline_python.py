#load pandas and matplotlib package
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pl

#Part 1: read data into data frame
andre = pd.read_csv('andre.csv')

#Part 1.5: quick EDA of data frame
print(andre.shape)
print(andre.columns)
print(andre.head())
print(andre.Year.value_counts) #First year is for 1976, so don't need to worry about earlier years than that in Part 2
print(andre.Year.dtype) #Year is in int64 format, meaning we can treat it numerically in Part 2

#Part 2: remove data from 1976 and after 1993
andre_subset = andre[(andre.Year > 1976) & (andre.Year <=1993)]
#check whether we were successful
print(andre_subset.shape) #fewer rows, same number of columns, as expected
print(andre_subset.Year.value_counts()) #No 1976, 1994, 1995, 1996. All good


#Part 3: make a histogram
#histogram of our subset, plotting hits ('H')
fig = pl.hist(andre_subset.H, bins = 100)
pl.title("Hits Histogram")
pl.savefig('andre_hits_hist_python.png')
