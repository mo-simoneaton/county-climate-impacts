import iris
import numpy as np
import pandas as pd
dir = '/home/joanna/METDataChallenge/maxdata/'
fileName = 'tasmax_rcp85_land-rcm_uk_12km_01_day_19901201-20001130.nc'

# load the cube.
cube = iris.load_cube(dir + fileName)

var1 = cube[0]

for year in range(1995,2000):
    Temp = var1.extract(iris.Constraint(year=year))
    days_over_30 = Temp.collapsed('time', iris.analysis.COUNT,
                                function=lambda values: values >= 30)
    iris.save(days_over_30, './maxdata/temp_over_30_95_00_{}.nc'.format(year))

filename = './maxdata/temp_over_30_95_00*.nc'
cubes = iris.load(filename)
cubes_all = cubes.concatenate()

av_days_over_30 = cubes_all[0].collapsed('time',iris.analysis.MEAN)
iris.save(av_days_over_30, './maxdata/temp_over_30_95_00_av.nc')

# 2025 to 2030
fileName = 'tasmax_rcp85_land-rcm_uk_12km_01_day_20201201-20301130.nc'

# load the cube.
cube = iris.load_cube(dir + fileName)

var1 = cube[0]

for year in range(2025,2030):
    Temp = var1.extract(iris.Constraint(year=year))
    days_over_30 = Temp.collapsed('time', iris.analysis.COUNT,
                                function=lambda values: values >= 30)
    iris.save(days_over_30, './maxdata/temp_over_30_25_30_{}.nc'.format(year))

filename = './maxdata/temp_over_30_25_30*.nc'
cubes = iris.load(filename)
cubes_all = cubes.concatenate()

av_days_over_30 = cubes_all[0].collapsed('time',iris.analysis.MEAN)
iris.save(av_days_over_30, './maxdata/temp_over_30_25_30_av.nc')

#2055-2060
fileName = 'tasmax_rcp85_land-rcm_uk_12km_01_day_20501201-20601130.nc'

# load the cube.
cube = iris.load_cube(dir + fileName)

var1 = cube[0]

for year in range(2055,2060):
    Temp = var1.extract(iris.Constraint(year=year))
    days_over_30 = Temp.collapsed('time', iris.analysis.COUNT,
                                function=lambda values: values >= 30)
    iris.save(days_over_30, './maxdata/temp_over_30_55_60_{}.nc'.format(year))

filename = './maxdata/temp_over_30_55_60*.nc'
cubes = iris.load(filename)
cubes_all = cubes.concatenate()

av_days_over_30 = cubes_all[0].collapsed('time',iris.analysis.MEAN)
iris.save(av_days_over_30, './maxdata/temp_over_30_55_60_av.nc')