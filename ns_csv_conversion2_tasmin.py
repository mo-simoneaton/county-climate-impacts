#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Joseph Elmes: NERC-Funded PhD Researcher in Applied Mathematics
University of Leeds : Leeds LS2 9JT : ml14je@leeds.ac.uk

Python 3.7
Created on Tue Mar 16 21:46:23 2021
"""
import numpy as np

def main(old_name, new_name, tasmin_threshold=2):
    import netCDF4
    import pandas as pd
    data = netCDF4.Dataset(old_name)
    tasmin = data['tasmin'][0] #Ensemble member 1

    nt, ny, nx = tasmin.shape #Time, y-grid, x-grid
    time = data['time'][:].astype(int)
    x = data['projection_x_coordinate'][:]
    y = data['projection_y_coordinate'][:]
    xx, yy = np.repeat(x, ny)[:, None], np.tile(y, nx)[:, None]

    data = tasmin.T.reshape((nx*ny, nt))
    data[data >  tasmin_threshold] = np.nan
    headers = np.concatenate([
        np.array(['projection_x_coordinate', 'projection_y_coordinate']),
        time
        ])

    data = np.concatenate([
        xx, yy, data
        ], axis=1)

    df = pd.DataFrame(data, index=None, columns=headers)
    df.to_csv(new_name, index=False,
          compression='gzip')

def loop_convert(directory, target_dir='/home/jonathan/Documents/Data/Met_Office_Data_Challenge/Daily_Selected_CSV_Tasmin'):
    import os
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for ncdf_file in os.listdir(directory):
        old_name = os.path.join(directory, ncdf_file)
        new_name = os.path.join(target_dir, ncdf_file.replace('.nc', '.csv.gz'))
        main(old_name, new_name)


if __name__ == '__main__':
    dir_to_ntcdf_files = '/home/jonathan/Documents/Data/Met_Office_Data_Challenge/Daily_Selected_Tasmin'
    loop_convert(dir_to_ntcdf_files)
