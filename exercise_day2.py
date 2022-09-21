import numpy
import pandas as pd
data=open("/Users/joells/PycharmProjects/day2_bio392/data.pgxseg")

datalines=data.readlines()
##print(datalines[1006:])

print(pd.DataFrame(datalines[1006:]))

data.close()
