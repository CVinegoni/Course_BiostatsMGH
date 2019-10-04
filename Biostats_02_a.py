#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: Biostats_02_a.py
# Project: Course_BiostatsMGH
# File Created: Friday, 4th October 2019 10:37:26 am
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Friday, 4th October 2019 10:37:26 am
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###

import pandas as pd
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(os.getcwd())
FILE_DIR = BASE_DIR.joinpath('Files\\02').joinpath('Practicum 1_dataset.csv')

data = pd.read_csv(FILE_DIR)
print(data.head())
print(data.info())
print(data.describe())

data['fatigcat'] = np.zeros(data.shape[0], dtype=int)
data.fatigcat = [0 if dep_value < 30 else 1 if (
    dep_value <= 40 and dep_value >= 30) else 2 if dep_value > 40 else '' for dep_value in data.fatig]
group_0 = data.groupby('fatigcat').get_group(0)
group_1 = data.groupby('fatigcat').get_group(1)
group_2 = data.groupby('fatigcat').get_group(2)


def cumulative_table_pd_column(column, list_values_to_cumulate):
    groups = [data.groupby(column).get_group(index)
              for index in list_values_to_cumulate]
    frequencies = np.array([g.shape[0] for g in groups])
    percentages = 100*frequencies/sum(frequencies)
    cum_frequencies = np.cumsum(frequencies)
    cum_percentages = np.cumsum(percentages)
    table = pd.DataFrame({'IDs': np.array(list_values_to_cumulate), 'Frequencies': frequencies,
                          'Percentages': percentages, 'Cumulative Freq.': cum_frequencies, 'Cumulative Perc.': cum_percentages})
    return table


table_pain = cumulative_table_pd_column('fatigcat', [0, 1, 2])

data['depressioncat'] = np.zeros(data.shape[0], dtype=int)
data.depressioncat = [0 if dep_value < 25 else 1 if (
    dep_value <= 36 and dep_value >= 25) else 2 if dep_value > 36 else 0 for dep_value in data.dep]
group_0 = data.groupby('depressioncat').get_group(0)
group_1 = data.groupby('depressioncat').get_group(1)
group_2 = data.groupby('depressioncat').get_group(2)

table_depression = cumulative_table_pd_column('depressioncat', [0, 1, 2])

