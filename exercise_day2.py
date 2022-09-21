import numpy
import pandas as pd
import matplotlib as plt
import csv

df=pd.DataFrame({})

data = open("/Users/joells/PycharmProjects/day2_bio392/data.pgxseg", newline='')
with data as segfile:
    for line in segfile.readlines():
        if '#' not in line:
            with open('data.csv', 'a+') as f:
                f.write(line)

datalines = data.readlines()

df=pd.read_csv('data.csv', sep='\t')
print('seg to dataframe')
