# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:10:40 2016

@author: Bhuti
"""
import pandas as pd
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 50)

got = pd.read_csv ('/Users/Bhuti/Desktop/war_of_the_five_kings_dataset-master/5kings_battles_v1.csv')
got = pd.DataFrame(got)
# print(got['attacker_size'])
print(got['defender_king'].value_counts())
got['defender_king'].value_counts().plot(kind='bar')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = got['year']
y = got['battle_number']
z = got['attacker_size']
# Axes3D.plot_surface('defender_1','battle_number','attacker_outcome')
Axes3D.plot_surface(x,y,z)