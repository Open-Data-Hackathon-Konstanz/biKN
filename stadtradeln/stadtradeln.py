#!/usr/bin/env python
# Display the Stadtadeln tiles

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextily as cx

inputfile = '../data/stadtradeln/Stadtradeln_RegionKonstanz_2020.csv'

# read file into dataframe
sr = pd.read_csv(inputfile, sep = ';', header = 0, index_col = False)

# convert to geodataframe to obtain points as extra column
gdf = gpd.GeoDataFrame(sr, geometry=gpd.points_from_xy(sr.lon, sr.lat))

# set coordinate reference system (CRS, EPSG:4326 is WSG84)
gdf = gdf.set_crs(epsg = 4326)

# either convert inputfile to OSM CRS (slow, but map is adjusted to window size)
# or convert OSM CRS to inputfile CRS (faster, but no adaptation)

# convert inputfile
#gdfwm = gdf.to_crs(epsg=3857)
#ax = gdfwm.plot(figsize=(10, 10), alpha = 1, column = "count", cmap = "viridis", markersize = 4, legend = True, 
#                norm = mpl.colors.LogNorm(vmin = gdfwm["count"].min(), vmax = gdfwm["count"].max()))

# convert OSM source
ax = gdf.plot(figsize=(10, 10), alpha = 1, column = "count", cmap = "viridis", markersize = 4, legend = True, 
                norm = mpl.colors.LogNorm(vmin = gdf["count"].min(), vmax = gdf["count"].max()))

#slightly unresponsive above zoom = 16
cx.add_basemap(ax, crs = gdf.crs, zoom = 13, source = cx.providers.OpenStreetMap.Mapnik)
#ax.scatter(gdfwm["geometry"].x, gdfwm["geometry"].y, color = gdfwm["count"])

plt.show()

