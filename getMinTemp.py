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

# Write out the result as nc file.
outFile = 'tasmin_rcp85_land-rcm_uk_12km_01_mon_1980-2080_Feb.nc'
iris.fileformats.netcdf.save(febTemp, dir + outFile)
