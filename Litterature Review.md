
# Seamless photovoltaic power generation forecasting

The aim of this research project is to propose a new power generation forecasting approach. This involves integrating predictions from various time frames using machine learning techniques applied to Global Horizontal Irradiance (GHI) time series data. By combining different predictions models, the study aims to achieve an accurate prediction of solar irradiance over a continuous time horizon.

## Objectives :
1-Complete a PV power forecasting state of the art.

2- Evaluating and programming  a linear relationship model between satellite and weather forecasting using linear regressions of past observations (Lorenz et al. 2012)[1]

3- Propose and evaluate more advanced machine learning methods and compare them to the reference method.

4- Set up a finer assessment according to parameters influencing the errors



 
## List of keywords

Arpège (Action de Recherche Petite Echelle Grande Echelle);
Analog Ensemble;
ANN (Artificial Neural Networks);
ARIMA (Auto Regressive Integrated Moving Average);
Clear-sky;
Cross-validation;
ECMWF (European Centre for Medium-Range Weather Forecasts);
ELM (Extreme Learning Machine);
GHI (Global Horizontal Irradiance);
GMDH (Group Method of Data Handling);
MAE (Mean Absolute Error);
Markov chains;
MBE (Mean Bias Error);
NNA (Neurole Network Approach);
NWP (Numerical Weather Prediction);
PV;
R: Pearson coefficient;
RFM (Random Forest Model);
RMSE (Root Mean Squared Error);
Satellite Imagery;
Seamless forecasting;
Site Instrumental de Recherche par Télédétection Atmosphérique (SIRTA);
Solar Zenith Angle (SZA);
SVM (Support Vector Machine)
 
## Relevant sources

In 1993, Murphy published in his paper "What is a good forecast?" [3] his definitions and insights that continue to be regarded and adhered to in the context of good forecasting. He defined three types of goodness to be satisfied in a prediction: consistency, quality, and value. To meet these different criteria, attention must be focused on the formulation, evaluation, and communication of the problem. This document is often cited as a reference for the approach to be followed in creating a good forecasting model.
Lorenz et al. (2012)[1] provide us a simplistic method of merging NWP and satellite forecasts, it contributes valuable insights to improving overall forecasting performance. It also provides us more inputs about different physical predictions model and their use in the time frame. Overall, this document serves as an excellent starting point for gaining insights into Seamless GHI forecasting.

In the context of GHI forecasting, several thorough reviews have been conducted. Notably, we can mention "Solar Photovoltaic Generation Forecasting Methods: A Review" by Sobri et al. (2018)[4] and "Machine Learning Methods for Solar Radiation Forecasting: A Review"  by Voyant et al. (2017) [5]. These two reviews provide a comprehensive overview of various GHI forecasting methods, categorizing them into four main groups: physical, statistical, machine learning, and hybrids. These publications are over 5 years old, so it is essential not to rely solely on them. However, they remain pivotal to our research, serving as a valuable resource by offering a thorough overview of existing models.

Finally, the last main document used in this research has been published by Cros and al (2020)[2]. Its aim is to study the reliability predictors for GHI Satellite-Based forecast. It provides us insight about two types of satellite models: clear-sky (clouds) and CMV field computation. The particularity of this paper is that it is using the same data we will use in our research.
 
## Context

In recent years, we have witnessed a surge in low-carbon regulations concurrently with a reduction in the manufacturing cost of solar panels. Consequently, an increasing number of households are being powered by solar energy. However, the primary challenge of solar energy lies in its inherent intermittency, as the amount of energy produced is directly linked to solar irradiance. The accurate prediction of energy output from solar panels based on Global Horizontal Irradiance (GHI) is therefore crucial for optimizing the efficiency of solar installations. There are multiple methodologies available to forecast solar irradiance. The predominant physical approaches revolve around satellite-based predictions, which are widely utilized for short-term intraday horizons (Cros et al. (2020)) [2], and Numerical Weather Prediction (NWP) models, which assume prominence in forecasting solar irradiance for day-ahead horizons. Additionally, statistical, numerical, and hybrid methods are also employed in this domain.

It is paramount to address this issue, as accurate prediction of solar energy production would enable optimal utilization of solar panels, efficient electricity distribution planning, and maximized economic returns from solar installations. Moreover, it would enhance the reliability and competitiveness of solar energy compared to conventional sources. This holds particularly true and significant for micro-grids, where precise forecasting plays a pivotal role in their functioning and success. 

Moreover, the economic viability of investors in the solar industry depends on precise predictions. Accurate forecasting allows for informed decision-making, efficient resource allocation, and reliable financial projections, ensuring long-term financial success. The demand for renewable energy is increasing every year and will continue to rise with the implementation of increasingly stringent environmental objectives. For instance, according to the Ministry of Ecological Transition, France aims to increase its share of renewable energy from 20 to 33 percent by 2030 [a]. Consequently, prediction errors could have significant repercussions on the overall electricity outcome. Furthermore, the implications of prediction errors extend beyond the specific context of the solar energy sector. Similar challenges are encountered in other domains, such as wind energy production, demand-side  management, and smart grids. Accurate forecasting of renewable energy production is vital for ensuring grid stability, optimizing energy generation and consumption, and supporting the global shift towards clean and sustainable energy sources.


 
## Literature review

Sobri et al. (2018) [4] classified prediction models into three categories: physical models, statistical models (encompassing both machine learning models and state transition models), and hybrid models (combinations of different models).

### Physical models
The physical satellite model involves interactions between solar radiation and atmospheric components, utilizing local meteorological data to eliminate the need for surface solar irradiance data. It is upadated every fifteen minutes (Cros et al 2020)[2] and used for Short-term forecasting (0 - 6 hours). Using linear regression to determine which prediction is the best for each time of the next 6h, Lorenz [1] determined in 2012 that using NWP was better after 4h. NWP models are based on the resolution of complex meteorological equations, they are mostly used for day-ahead forecasting. Additionally, sky imagery, using devices like Total Sky Imager (TSI), is employed for short-term cloud cover, irradiance, and power predictions. The application of satellite imaging, which relies on visible and infrared images from geostationary satellites, is also discussed in Sobra and al’s review.

### Linear Regression
Discontinuities between time frames or in forecast values from the same horizon can be observed using physical models. To obtain a more accurate seamless forecast a lot of different statistical models have been developed in the past two decades. The linear regression model as proposed by Lorenz et al. (2012) [1] to enhance short-term forecasting by combining satellite data and NWP. Their approach optimally weighed data sources based on the forecast horizon and corrected systematic deviations. In regional day-ahead forecasting, they combined two NWP model forecasts, resulting in a ten percent improvement compared to the ECWMF-based forecast. Additionally, for intra-day forecasting, they incorporated satellite-based Satellite forecasts, yielding even better results. While this study represents an initial, somewhat simplistic method of merging NWP and satellite forecasts, it contributes valuable insights to improving overall forecasting performance. But may struggle to capture complex temporal patterns or dependencies. That why more sophisticated regression such as Autoregressive model have been developed. 

### Autoregression
Autoregressive models have been used for more than 50 years to predict time series values (Akaike and al 1969) [6] and is widely used in finance predictions. In terms of GHI forecasting, researchers usually combined this methods with other machine learning methods to enhance them. It is usually combined with ANN (Lima and al 2016) [7] or with RFM (Agoula and al 2017) [8]. Different type of Autoregressive models are explored in the literature and well described by Li and al (2016) [9].
Time series models, treating power output as a time-dependent variable, include auto-regressive (AR), moving average (MA), and their combinations like auto-regressive moving average (ARMA) and auto-regressive integrated moving average (ARIMA), commonly known as Box-Jenkins models. Studies have applied time series models for short-term solar power prediction, with some specifically using the ARIMA model without exogenous inputs. To incorporate external factors into the time series model, the ARMAX model is employed, proven as a robust tool in time series forecasting. Some studies have demonstrated the superiority of the ARX model with numerical weather conditions (NWPs) as inputs over the AR model in forecasting short-term (2-hour ahead) power output. The ARMAX model has also been applied to forecast the power output of a grid-connected PV system, incorporating exogenous inputs.

### Markov Chain
Sobri et al (2018) [4] also showcase the application of Markov chain models in solar radiation prediction and PV system power generation forecasting, demonstrating their effectiveness in capturing dependencies between states and transitions. The system comprises connected states, where the next state depends solely on the current state. Transitions between states are governed by transition probabilities.

### ANN

ANN models can be used to classified complex non-linear data. The accuracy of the prediction depends on input parameters, training algorithm, and structure configuration [10]. A review focuses on predicting solar radiation using various Artificial Neural Network (ANN) techniques was proposed in 2014 by Yadav et al.[10]. The discussed ANN models in the paper offer improved accuracy compared to Ångström model, conventional, linear, non-linear, and fuzzy logic models. Geographical and meteorological parameters are used as input variables for ANN models in solar radiation prediction. Sunshine hours and air temperature prove to be effective inputs with a high correlation coefficient of 97.65%. A lot of divers ANN are discussed in this review, and, in general, a lot of ANN models have been detrailed in the litteratur for GHI forecasting. The review separate ANN models in two categories depending on the time horizon efficiency (short term and intraday). 
IN 2010, melti et al proposed an ANN-MLP (Multi Layer Perceptron) architecture for forecasting 24-h ahead [11].The input layer accepts as parameters the mean daily solar irradiance, the mean daily air temperature and the day of the month, while the output layer gives as parameters the 24 h of GHI at the next day. MLP have been chosen for it easy implementation compared to ANN hybrids. In the litterature a MLP with the back-propagation (BP) training algorithm is used. In melti paper, K-fold cross-validation technique have been used to evaluate the MLP model and compare it to Fuzzy Logic and RNN (recurrent neural network). MLP efficiency will grandly depends on the right choice of hidden layers. The RMSE from the 10-fold cross-validation error was used to choose this number. K was set to 10. As a result the correlation coefficient is more than 98%, while for cloudy days is less then 95%. In the dicussion part the idea of using more data to improve the model is discussed.


## Resources

[a] Objectif 2030 et situation actuelle de la France | Chiffres clés des énergies renouvelables (developpement-durable.gouv.fr)

[1]Lorenz, E., Kuehnert, Jan & Heinemann, Detlev 2012 Short term forecasting of solar irradiance by combining satellite data and numerical weather predictions .

[2]Cros, Sylvain, Badosa, Jordi, Szantaï, André & Haeffelin, Martial 2020 Reliability predictors for solar irradiance satellite-based forecast. Energies 13 (21).

[3]Murphy, Allan H. 1993 What is a good forecast? an essay on the nature of goodness in weather forecasting. Weather and Forecasting 8 (2), 281 – 293.

[4]Sobri, Sobrina, Koohi-Kamali, Sam & Rahim, Nasrudin Abd. 2018 Solar photovoltaicgeneration forecasting methods: A review. Energy Conversion and Management 156, 459–497.

[5]Cyril Voyant, Gilles Notton, Soteris Kalogirou, Marie-Laure Nivet, Christophe Paoli, Fabrice Motte, Alexis Fouilloy,Machine learning methods for solar radiation forecasting: A review,Renewable Energy,Volume 105,2017,Pages 569-582

[6]Akaike, H. (1969). Fitting autoregreesive models for prediction. In Selected Papers of Hirotugu Akaike (pp. 131-135). New York, NY: Springer New York.

[7]Lima, F. J., Martins, F. R., Pereira, E. B., Lorenz, E., & Heinemann, D. (2016). Forecast for surface solar irradiance at the Brazilian Northeastern region using NWP model and artificial neural networks. Renewable Energy, 87, 807-818.

[8]Agoua, X. G., Girard, R., & Kariniotakis, G. (2017). Short-term spatio-temporal forecasting of photovoltaic power production. IEEE Transactions on Sustainable Energy, 9(2), 538-546.

[9]Li, Y., He, Y., Su, Y., & Shu, L. (2016). Forecasting the daily power output of a grid-connected photovoltaic system based on multivariate adaptive regression splines. Applied Energy, 180, 392-401.

[10]Yadav, A. K., & Chandel, S. S. (2014). Solar radiation prediction using Artificial Neural Network techniques: A review. Renewable and sustainable energy reviews, 33, 772-781.

[11] Mellit A, Pavan AM. A 24-h forecast of solar irradiance using artificial neuralnetwork: application for performance prediction of a grid-connected PV plant at Trieste, Italy. Sol Energy 2010;84:807–21.
