#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Joseph Elmes: NERC-Funded PhD Researcher in Applied Mathematics
University of Leeds : Leeds LS2 9JT : ml14je@leeds.ac.uk

Python 3.7
Created on Tue Mar 16 17:21:54 2021
"""
import numpy as np

def main(old_name, new_name, tasmax_threshold=24):
    import os, netCDF4
    import pandas as pd
    data = netCDF4.Dataset(old_name)
    tasmax = data['tasmax'][0] #Ensemble member 1

    nt, ny, nx = tasmax.shape #Time, y-grid, x-grid
    time = data['time'][:]
    x = data['projection_x_coordinate'][:]
    y = data['projection_y_coordinate'][:]
    xx, yy = np.repeat(x, ny)[:, None], np.tile(y, nx)[:, None]

    data = tasmax.T.reshape((nx*ny, nt))
    nloc, nt = np.where(data > tasmax_threshold)
    x_new, y_new = xx[nloc, 0], yy[nloc, 0]
    time = time[nt]
    data_new = data[nloc, nt]

    data_dic = {
        'projection_x_coordinate' : x_new,
        'projection_y_coordinate' : y_new,
        'Time' : time,
        'tasmax' : data_new}

    df = pd.DataFrame(data_dic, index=None)
    df.to_csv(new_name, index=False,
          compression='gzip')

def loop_convert(directory, target_dir='CSV_OUTPUT'):
    import os
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for ncdf_file in os.listdir(directory):
        old_name = os.path.join(directory, ncdf_file)
        new_name = os.path.join(target_dir, ncdf_file.replace('.nc', '.csv.gz'))
        main(old_name, new_name)


if __name__ == '__main__':
    dir_to_ntcdf_files = 'Data/NC'
    loop_convert(dir_to_ntcdf_files)