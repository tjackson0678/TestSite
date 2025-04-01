import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('python/ECGR5105/Housing.csv')
#df =pd.read_csv('https://raw.githubusercontent.com/satishgunjal/datasets/master/univariate_profits_and_populations_from_the_cities.csv')
print(df.head()) # To get first n rows from the dataset default value of n is 5