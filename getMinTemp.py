#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeremy Walton : jeremy.walton@metoffice.gov.uk
Python 3.7
"""

import iris
import numpy as np

dir = '/scratch/jwalton/'
fileName = 'tasmin_rcp85_land-rcm_uk_12km_01_mon_198012-208011.nc'

# load the cube.
cube = iris.load_cube(dir + fileName)

# first dimension is the variant - pull this out.
var1 = cube[0]
print(var1.shape)

# Extract all the temperatures from February (month 2).
febTemp = var1.extract(iris.Constraint(month_number=lambda cell: 2 == cell))
print(febTemp)

# Get the range of values.
minTemp = np.amin(febTemp.data)
maxTemp = np.amax(febTemp.data)
print("Range is", minTemp, "to", maxTemp)

# Extract the data for a group of sub-periods, and output it in separate files.
years = [[1995, 2000],
         [2025, 2030],
         [2055, 2060]]

for limits in years:
    # Extract all data in this period.
    yearFebTemp = febTemp.extract(iris.Constraint(year=lambda cell: limits[0] <= cell <= limits[1]))
    
    # Write out the result as nc file.
    outFile = 'tasmin_rcp85_land-rcm_uk_12km_01_mon_%d-%d_Feb.nc' % (limits[0], limits[1])
    iris.fileformats.netcdf.save(yearFebTemp, dir + outFile)
