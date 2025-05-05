#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 18:30:19 2025

@author: jonathansmacbook
"""
# Import Modules
import geopandas as gpd

import matplotlib.pyplot as plt

# Load DC census tract shapefile
geodata = gpd.read_file("Input Information/DCtl_2024_11_tract.zip")

# Project to a metric CRS for analysis 
geodata = geodata.to_crs(epsg=26918)  

# Save the reprojected file to a GeoPackage to use for later scripts 
geodata.to_file("DCMap.gpkg", layer="DCMAP")

# Create plot
fig, ax = plt.subplots(dpi=300)

# Plot the DC boundary in light grey (Tip: The light grey I found to be the easiest to layer additional information on) 
geodata.plot(ax=ax, color="lightgrey")

# Remove axis (Tip: I did not find the axis to be helpful for my analysis, but you can choose to keep it if you find it helpful for your analysis) 
ax.axis("off")

# Add title to the map
ax.set_title("Washington, DC Boundary")

# Save plot as a PNG file
plt.savefig("Map Images/WashingtonDCMap.png", dpi=300)

