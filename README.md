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
This informations concerned the GHI prediction of the NRlab located in Palaiseau for period of three years from summer of 2017 to summer of 2020. Some values are missing (338 rows out of over 44800) in addition to some inconvenient holes in the data set. In particular, the values of september 2018 are all missing.
#### Columns description :

