## Heatwave Impacts

### Goal

To identify those unitary authorities most likely to experience more heatwaves over the target time periods.

### Heatwave definition

From the Met Office website:

"A UK heatwave threshold is met when a location records a period of at least three consecutive days with daily maximum temperatures meeting or exceeding the heatwave temperature threshold. The threshold varies by UK county, see the UK temperature threshold map below."

![image](https://user-images.githubusercontent.com/35728981/111479578-03acd780-8729-11eb-87bf-2f3e415e6c2d.png)

For further info on heatwaves see [here](https://www.metoffice.gov.uk/weather/learn-about/weather/types-of-weather/temperature/heatwave).

### Source data

The [UKCP18 UK Climate Projections](https://github.com/COP26-Hackathon/Met-Office-Climate-Data-Challenge-March_2021/wiki/Data-Sources#uk-climate-projections).

### Methodology

The following steps were carried out to calculate the likely number of heatwaves per unitary authority per time period:

1. Download the daily tasmax (temperature-at-surface maximum) data for all ensemble model members for all the years required. Use the CEDA Archive, e.g. https://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/01/tasmax/day/latest which lists all the daily tasmax data for the 01 ensemble model member in files divided by decade, e.g. rcm_uk_12km_01_day_20501201-20601130.nc

2. Execute [this Python script](https://github.com/mo-simoneaton/county-climate-impacts/blob/master/ns_csv_conversion2_tasmin.py) to replace temperature values <=24 with NaN to reduce filesize whilst maintaining time series integrity and convert to CSV.

3. Execute [this R script](https://github.com/mo-simoneaton/county-climate-impacts/blob/master/Testing%20heatwave%20classification.Rmd) to identify heatwave events in the CSV files where a heatwave event = 3 consecutive days where the max temp >= the regional threshold for that grid cell.

4. TODO
