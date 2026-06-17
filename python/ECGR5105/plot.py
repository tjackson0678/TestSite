import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))

# create a simple dataset of people
df = pd.read_csv('python/ECGR5105/Energy.csv')