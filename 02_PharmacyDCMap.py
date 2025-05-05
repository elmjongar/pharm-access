#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 7:38:09 2025

@author: jonathansmacbook
"""
# Import Modules
import geopandas as gpd

import matplotlib.pyplot as plt

# Load DC boundary map from previously saved GeoPackage 
geodata = gpd.read_file("DCMap.gpkg", layer="DCMAP")

# Load pharmacy locations 
DCPharm = gpd.read_file("Input Information/Pharmacy_Locations.zip")

# Set the display CRS for consistent map visualization across the DCMap and the Pharmacy Locations 
epsg_display = 6350

geodata = geodata.to_crs(epsg=epsg_display)

DCPharm = DCPharm.to_crs(epsg=epsg_display)

# Save reprojected pharmacy data to GeoPackage 
DCPharm.to_file("PharmMap.gpkg", layer="PharmLayer") 

# Create figure 
fig, ax = plt.subplots(dpi=300)

# Plot DC boundary 
geodata.plot(ax=ax, color="lightgrey")

# Plot pharmacy locations as yellow dots and add label for the legend (Tip: Visual accessibility is incredibly important, ensure that the dots and the eventual buffers created for this analysis are accessible to people who may have color vision deficiency)
DCPharm.plot(ax=ax, color="yellow", markersize=2, label="Pharmacies")

# Add legend in the bottom-left corner
ax.legend(loc="lower left", fontsize=6, frameon=True)

# Remove axis (Tip: I did not find the axis to be helpful for my analysis, but you can choose to keep it if you find it helpful for your analysis) 
ax.axis("off")

# Add map title
ax.set_title("Washington, DC Map with Pharmacy Locations", fontsize=8)

# Save the figure as a PNG image 
plt.savefig("Map Images/DCMapwithPharmacyLocations.png", dpi=300)