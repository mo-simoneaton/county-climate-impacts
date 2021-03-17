## Heatwave Impacts

### Goal

To identify those unitary authorities most likely to experience more heatwaves over the target time periods.

### Heatwave definition

From the Met Office website:

"A UK heatwave threshold is met when a location records a period of at least three consecutive days with daily maximum temperatures meeting or exceeding the heatwave temperature threshold. The threshold varies by UK county, see the UK temperature threshold map below."

![image](https://user-images.githubusercontent.com/35728981/111479578-03acd780-8729-11eb-87bf-2f3e415e6c2d.png)

For further info on heatwaves see [here](https://www.metoffice.gov.uk/weather/learn-about/weather/types-of-weather/temperature/heatwave).

### Outputs

An [interactive map](https://gdsl.carto.com/u/natalie-envs456-19/builder/bbaadca7-7e88-408c-a56b-10e71ce01494/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B46.98025235521883%2C-16.545410156250004%5D%2C%22sw%22%3A%5B62.20651189841766%2C9.953613281250002%5D%2C%22center%22%3A%5B55.31664304437719%2C-3.2958984375000004%5D%2C%22zoom%22%3A6%7D%7D) based on the heatwave event data. Credit: Natalie Rose

### IMPORTANT

There's currently some noise in the heatwave events data. Some double-counting of days contributing to heatwave events means the numbers are skewed upwards. Adjustment is needed in [this R code](https://github.com/mo-simoneaton/county-climate-impacts/tree/master/Heatwave%20classifier) to return accurate results. The visual still indicates a trend, but the numerical values are out.

### Source data

The [UKCP18 UK Climate Projections](https://github.com/COP26-Hackathon/Met-Office-Climate-Data-Challenge-March_2021/wiki/Data-Sources#uk-climate-projections).

### Methodology

The following steps were carried out to calculate the likely number of heatwaves per unitary authority per time period:

1. Download the daily tasmax (temperature-at-surface maximum) data for all ensemble model members for all the years required. Use the CEDA Archive, e.g. https://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/01/tasmax/day/latest which lists all the daily tasmax data for the 01 ensemble model member in files divided by decade, e.g. rcm_uk_12km_01_day_20501201-20601130.nc

2. Execute [this Python script](https://github.com/mo-simoneaton/county-climate-impacts/blob/master/ns_csv_conversion2_tasmin.py) to replace temperature values <=24 with NaN to reduce filesize whilst maintaining time series integrity and convert to CSV.

3. Execute [this R code](https://github.com/mo-simoneaton/county-climate-impacts/tree/master/Heatwave%20classifier) to identify heatwave events in the CSV files where a heatwave event = 3 consecutive days where the max temp >= the regional threshold for that grid cell.

4. TODO

