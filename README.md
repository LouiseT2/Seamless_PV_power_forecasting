# Seamless_PV_power_forecasting
Seamless prediction of GHI using machine learning

The aim of this research project is to propose a new power generation forecasting approach. This involves integrating predictions from various time frames using machine learning techniques applied to Global Horizontal Irradiance (GHI) time series data. By combining different predictions models, the study aims to achieve an accurate prediction of solar irradiance over a continuous time horizon.


## Objectives :

1-Complete a PV power forecasting state of the art.

2- Evaluating and programming  a linear relationship model between satellite and weather forecasting using linear regressions of past observations (Lorenz et al. 2012)

3- Propose and evaluate more advanced machine learning methods and compare them to the reference method.

4- Set up a finer assessment according to parameters influencing the errors

## Dataset description :
The data used in this project comes from E4C. It is composed of 25 .csv files which each contains 9 exact same columns (containing the same data):date,Sirta_GHI,Clearsky_GHI,Arpege_GHI,SZA,Kc_Sat_mean,Kc_Sat_std,Kc_obs and Wreg. And one different column correponding to the GHI Satelitte prediction, each one from a different time horizon but for the same time prediction. 
This informations concerned the GHI prediction of the SIRTA observatory located in Palaiseau (France, ‘48.713◦ N; 2.208◦ E’, 157 m above average sea level) for period of three years from summer of 2017 to summer of 2020. Each row refers to a date with a specific time, data have been collected each day between 5:11:00 and 19:11:00 every 15 minutes meaning we have 57 rows for each day.
Some values are missing (338 rows out of over 44800) in addition to some inconvenient holes in the data set. In particular, the values of september 2018 are all missing.
### Columns description :
**Sirta_GHI:** Sirta_GHI correspond to the GHI observed at the SIRTA observatory, this is our target value which we try to predict. It has been observed at 1 min temporal resolution by a pyranometer (Kipp and Zonen CM22)

**Clearsky_GHI:** Based on satellite images determine for each pixel if there are clouds or not. Then determine using Heliosat method the GHI. Usually used for intra-day forcasting.

**Arpege_GHI:** 
The NWP (Numerical Weather Prediction) model ARPEGE is utilized by Météo-France as an operational forecast model. It provides forecasts globally with a horizontal resolution of approximately 7.5 km over mainland France. The model's output, specifically "surface solar radiation downwards," serves as a reference for assessing satellite-based forecasts. ARPEGE employs a 4D-Var data assimilation method for determining initial conditions based on observations. This spectral hydrostatic model run daily at 12:00 UTC for a 0–24 hour forecast period with hourly time resolution. The spatial resolution of this global model is 5 km over Europe, and outputs are linearly interpolated to align with MSG (Meteosat Second Generation) timestamps. Usually used for day-ahead forcasting.

**SZA:** Solar Zenith Angle, describes the daily and seasonal course of the Sun. SZA values are computed through the Solar Position Algorithm (SPA).

**Kc_Sat_mean and Kc_Sat_std:** Kc correspond to Clear-sky index, a variable used  to quantify the amount of solar radiation reaching the Earth's surface under clear-sky conditions in comparison to the potential maximum solar radiation at that location. A Kc value of 1 indicates perfect clarity, meaning the observed solar radiation matches the potential maximum under clear-sky conditions. Values less than 1 indicate a reduction in solar radiation due to atmospheric factors. Kc_Sat_mean represents the spatial mean of Kc_Sat (Kc calculated from satelite measurment) on 50km around SIRTA Observatory. Meanwhile, Kc_Sat_std is the standard deviation of Kc_Sat on 50km around SIRTA Observatory.

**Kc_obs:** Kc_obs is the clear-sky index from real time observed GHI. Meaning Kc_obs=GHIobs/GHIclear-sky.

**Wreg:** The Wreg column contains integers from 1 to 4 corresponding to the four possible Weather Regime in the SIRTA area. This Weather Regime are NAO-((Negative Northern Atlantic Oscillation): anticyclone coming from the north west, brings cold, wet, clouds...; Atlantic Ridge: anticyclone from the middle of Atlantic Ocean; Scandinavian Blocking: anticyclone from North Sea and NAO+(Positive Northern Atlantic Oscillation): Zonal circulation, bring dry, warm, not many clouds...
