

import pandas as pd
import os
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


BASE_DIR = Path(os.getcwd())
FILE_DIR = BASE_DIR.joinpath('Files\\01').joinpath('Practicum 1_dataset.csv')


data = pd.read_csv(FILE_DIR)
print(data.head())
print(data.info())
print(data.describe())
percentages = [0.25, 0.50, 0.75]
quantile_data_1 = tuple(data.pcs.dropna() .quantile(percentage)
                        for percentage in percentages)
quantile_data_2 = [np.percentile(data.pcs.dropna().to_numpy(), percentage*100)
                   for percentage in percentages]
pcs_array = data.pcs.to_numpy()
pcs_array = pcs_array[pcs_array == pcs_array]
quantile_data_3 = [np.percentile(pcs_array, percentage*100)
                   for percentage in percentages]

min_1 = data.pcs.dropna().min()
max_1 = data.pcs.dropna().max()

min_2 = pcs_array.min()
max_2 = pcs_array.max()

mean_value = np.mean(pcs_array)

interquartile_range = abs(quantile_data_1[2]-quantile_data_1[1])

print(20*'*' + '\n' + '5 numbers stats' + '\n \n')
print('Mean:\t' + str(mean_value))
print('Median:\t' + str(quantile_data_1[1]))
print('Min:\t' + str(min_1))
print('Max:\t' + str(max_1))
print('First Quartile (25%):\t' + str(quantile_data_1[0]))
print('First Quartile (75%):\t' + str(quantile_data_1[2]))
