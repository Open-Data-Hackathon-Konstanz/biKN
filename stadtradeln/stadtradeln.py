#!/usr/bin/env python
# Display the Stadtadeln tiles

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextily as cx

inputfile = '../data/stadtradeln/Stadtradeln_RegionKonstanz_2020.csv'

# first, import data for cycling ways, for more information
# for more information see geojson_info.txt
cyc = gpd.read_file("cyclingways.geojson")
cyc = cyc.to_crs(epsg = 3857)


# read file into dataframe
sr = pd.read_csv(inputfile, sep = ';', header = 0, index_col = False)

# if desired, select only hexagons, which are hit more often
#sr = sr[sr["count"] > 2000]

# convert to geodataframe to obtain points as extra column
gdf = gpd.GeoDataFrame(sr, geometry = gpd.points_from_xy(sr.lon, sr.lat))

# set coordinate reference system (CRS, EPSG:4326 is WSG84)
gdf = gdf.set_crs(epsg = 4326)

# either convert inputfile to OSM CRS (slow, but map is adjusted to window size)
# or convert OSM CRS to inputfile CRS (faster, but no adaptation)
# CRS = coordinate reference system

# CONVERT inputfile
gdfc = gdf.to_crs(epsg = 3857)

# plot with color gradient (viridis or OrRd
ax = gdfc.plot(figsize=(10, 6), alpha = 1, column = "count", cmap = "OrRd", markersize = 4, legend = True,
                norm = mpl.colors.LogNorm(vmin = gdfc["count"].min(), vmax = gdfc["count"].max()))

# plot without color gradient
#ax = gdfc.plot(figsize=(10, 6), alpha = 1, markersize = 3, color = "red")

# add OSM basemap
#cx.add_basemap(ax, zoom = 13, source = cx.providers.CyclOSM)
#cx.add_basemap(ax, zoom = 14, source = cx.providers.OpenStreetMap.Mapnik, alpha = 0.5)

# CONVERT OSM source
#ax = gdf.plot(figsize=(10, 10), alpha = 1, column = "count", cmap = "viridis", markersize = 4, legend = True, 
#                norm = mpl.colors.LogNorm(vmin = gdf["count"].min(), vmax = gdf["count"].max()))
#cx.add_basemap(ax, crs = gdf.crs, zoom = 16, source = cx.providers.OpenStreetMap.Mapnik)

# plot cycling ways
cyc.plot(ax = ax, markersize = 0.1, alpha = 0.6)

plt.title("Ausgebaute Fahrradwege und Häufigkeit, mit der ein Hexagon durchfahren wurde (logarithmisch!)")
plt.xlim([1005000,1030000])
plt.ylim([6047500,6066000])

plt.show()

