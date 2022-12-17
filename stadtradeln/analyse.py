#!/usr/bin/env python
# Some visualization of the Stadtradeln data

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextily as cx

# files of different years
in20 = '../data/stadtradeln/Stadtradeln_RegionKonstanz_2020.csv'
in19 = '../data/stadtradeln/Stadtradeln_RegionKonstanz_2019.csv'
in18 = '../data/stadtradeln/Stadtradeln_RegionKonstanz_2018.csv'

# read files into dataframe
sr20 = pd.read_csv(in20, sep = ';', header = 0, index_col = False)
sr19 = pd.read_csv(in19, sep = ';', header = 0, index_col = False)
sr18 = pd.read_csv(in18, sep = ';', header = 0, index_col = False)

# value_counts counts the the number of hexagons which are hit x times

# either aggregate the hexagons which are hit x times into bins to get a good display
an20 = pd.cut(sr20['count'], bins=100, precision = 0).value_counts()
an19 = pd.cut(sr19['count'], bins=100, precision = 0).value_counts()
an18 = pd.cut(sr18['count'], bins=100, precision = 0).value_counts()

# or display all values directly
#an20 = sr20["count"].value_counts()
#an19 = sr19["count"].value_counts()
#an18 = sr18["count"].value_counts()

# sort by index, so hexagons which are hit one time are at the origin
an20 = an20.sort_index()
an19 = an19.sort_index()
an18 = an18.sort_index()

# plot, eiher with or without log
ax = an20.plot( kind = "bar", logy = True, zorder = 0)
#an19.plot(ax = ax, kind = "bar", logy = False, color = "red", zorder = 1)
#an18.plot(ax = ax, kind = "bar", logy = False, color = "green", zorder = 2)

#plt.xlim([0, 100]) # set limits if desired
plt.title("Stadtradeln 2020: Verteilung der Trefferraten der Hexagons. Gelesen: Es gib über 70000 (y-Werte) Hexagone, die zwischen 0 und 113 (x-Werte) mal getroffen werden")
plt.ylabel("Count of hexagon which is hit x times")

plt.show()
