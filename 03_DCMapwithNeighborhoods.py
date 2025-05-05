#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 20:09:56 2025

@author: jonathansmacbook
"""
# Import Modules
import geopandas as gpd

import matplotlib.pyplot as plt

# Load DC boundary from previously saved GeoPackage
geodata = gpd.read_file("DCMap.gpkg", layer="DCMAP")

# Load pharmacy locations from previously saved GeoPackage
PharmLayer = gpd.read_file("PharmMap.gpkg", layer="PharmLayer")

# Load neighborhood clusters shapefile
DCNeighborhoods = gpd.read_file("Input Information/Neighborhood_Clusters.zip")

# Save neighborhood data to GeoPackage
DCNeighborhoods.to_file("DCMapwithNeighborhood.gpkg", layer="DCNeighborhoodMAP") 


# Set the display CRS for consistent map visualization across the DCMap, Pharmacy Locations, and Neighborhood Boundaries
epsg_display = 3857

geodata = geodata.to_crs(epsg=epsg_display)

PharmLayer = PharmLayer.to_crs(epsg=epsg_display)

DCNeighborhoods = DCNeighborhoods.to_crs(epsg=epsg_display)

# Create figure
fig, ax = plt.subplots(dpi=400)

# Plot DC boundary
geodata.plot(ax=ax, color="lightgrey")

# Plot neighborhood boundaries with transparent fill and thin black outline (Tip: Transparent fill is crucial to showcase the pharmacy locations)
DCNeighborhoods.plot(ax=ax, facecolor="none", edgecolor="black", linewidth=0.2)

# Plot pharmacy locations as yellow dots and add label for the legend (Tip: Visual accessibility is incredibly important, ensure that the dots and the eventual buffers created for this analysis are accessible to people who may have color vision deficiency)
PharmLayer.plot(ax=ax, color="yellow", markersize=2, label="Pharmacies")

# Add legend in the bottom-left corner
ax.legend(loc="lower left", fontsize=6, frameon=True)

# Remove axis (Tip: I did not find the axis to be helpful for my analysis, but you can choose to keep it if you find it helpful for your analysis) 
ax.axis("off")

# Add map title 
ax.set_title("Pharmacies and Neighborhood Boundaries", fontsize=8)

# Save figure as a PNG file
plt.savefig("Map Images/DCMapwithPharmaciesandNeighborhoodBoundaries.png", dpi=300)