import os
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# import seaborn as sns 
# from scipy.stats import mode, skew


house_price = pd.read_csv('train.csv')
print(house_price.shape)
print()