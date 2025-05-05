#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 18:52:17 2025

@author: jonathansmacbook
"""
# Import Modules
import geopandas as gpd

import matplotlib.pyplot as plt

# Load previously saved DC boundary map
geodata = gpd.read_file("DCMap.gpkg", layer="DCMAP")

# Load pharmacy locations from previously saved GeoPackage
PharmLayer = gpd.read_file("PharmMap.gpkg", layer="PharmLayer")

# Load DC neighborhood boundaries from GeoPackage
DCNeighborhoods = gpd.read_file("DCMapwithNeighborhood.gpkg", layer="DCNeighborhoodMAP")

# Set the display CRS for consistent map visualization across the DCMap, Pharmacy Locations, and Neighborhood Boundaries
epsg_buffer = 3857
geodata = geodata.to_crs(epsg=epsg_buffer)
PharmLayer = PharmLayer.to_crs(epsg=epsg_buffer)
DCNeighborhoods = DCNeighborhoods.to_crs(epsg=epsg_buffer)

# Create a copy of the pharmacy layer to create a 1-mile (1609.34 meters) buffers
PharmBuffer = PharmLayer.copy()
PharmBuffer["geometry"] = PharmLayer.buffer(1609.34)

# Save buffer layer to GeoPackage 
PharmBuffer.to_file("PharmMap.gpkg", layer="PharmBuffer")

# Create figure 
fig, ax = plt.subplots(dpi=300)

geodata.plot(ax=ax, color="lightgrey", edgecolor="none")

# Overlay neighborhood boundaries with no fill and thin black outline (Tip: Ensure that the linewidth of the boundaries is not too thick, otherwise they have the possibility of covering crucial information)
DCNeighborhoods.plot(ax=ax, facecolor="none", edgecolor="black", linewidth=0.2)

# Plot 1-mile pharmacy buffers in semi-transparent purple (Tip: Ensure that it’s semi-transparent, as when the circles overlap, you can more easily identify areas that are covered by multiple pharmacies because these areas will be a darker shade of purple.)
PharmBuffer.plot(ax=ax, facecolor="purple", edgecolor="none", alpha=0.1, label="1-Mile Pharmacy Buffer")

# Plot pharmacy points in yellow and add label for legend (REMINDER: Visual accessibility is incredibly important, ensure that the dots and the buffers created for this analysis are accessible to people who may have color vision deficiency)
PharmLayer.plot(ax=ax, color="yellow", markersize=2, label="Pharmacies")

# Remove axis (Tip: I did not find the axis to be helpful for my analysis, but you can choose to keep it if you find it helpful for your analysis) 
ax.axis("off")

# Add map title 
ax.set_title("Washington, DC Map with Pharmacy Locations and One Mile Buffers", fontsize=8)

# Add legend in the bottom-left corner
ax.legend(loc="lower left", fontsize=6, frameon=True)

# Save figure as a PNG file
plt.savefig("Map Images/DCMapwithPharmacyBuffers.png", dpi=300)





