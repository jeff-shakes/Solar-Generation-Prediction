# Solar Energy Generation Prediction

## Table of Contents
* data
  * cleaned
  * raw
* images

* presentation
  * slides
* code
  * 01 - Data Cleaning
    * 01 - Data Cleaning

  * 02 - EDA_Preprocessing
    * 02 - EDA
    * 03 - Preprocessing

  * 03 - Modeling
    * 04 - Modeling
    * 05 - Univariate_Modeling
    * 06 - Multivariate_Modeling
    * 07 - Modeling_Other_Campuses_Sites
    
  * 04 - Modeling
    * solar_generation_streamlit.py
#####

---
## Background
Due to the variable nature of renewable energies (i.e., energies reliant on conditions such as cloudiness for solar or windiness for wind energy), as well as the uncertainty and variability in each renewable energy site's component architecture, predicting the power generation from each site is challenging. Consequently, the integration of solar energy generation sites with larger electrical grids can be complicated. One way of easing this burden is accurately reporting and predicting power generation from these variable generation sites.

---
## Problem Statement
 Using the solar generation output of a specific solar farm site, along with the corresponding weather data, can a model predict the solar generation output of that specific site within a mean-absolute-error score of less than 10% of max output?

 Furthermore, can the same model architecture optimized for a specific site be used to predict the generation of another site or even another entire campus?

---
## Who This Concerns
 This investigation was carried out for research purposes and designed to be utilized in both small-scale and large-scale solar energy generation stations for optimizing operational outcomes at a site level. Moreover, accurate generation predictions are necessary for integration within the larger electric grid and help determine the amount of electricity demand renewables will provide for - allowing less waste in the electricity derived from non-renewable sources.

 Also, suppose the model for a single site can be used to predict other sites or even whole campuses. In that case, the modeling process does not need to be iterated for each location, saving time and resources.

---
## Python Libraries
Following python libraried were used during the project:
  - `pandas`
  - `numpy`
  - `seaborn`
  - `matplotlib`
  - `sklearn`
  - `sktime`
  - `statsmodel`
  - `keras`
  - `tensorflow`
  

## Notebooks
  - `Jupyter Lab`
  - `Google Colab`
  

## Models Investigated
  - `ARIMA`
  - `Univariate RNN with SimpleRNN and Dense Layers`
  - `Multivariate RNN with LTSM, SimpleRNN and Dense Layers`

---
## Datasets
For this project, a dataset was used that incorporated:
1. Solar power generation for different solar sites at different campuses at La Trobe University, Victoria, Australia. This includes photovoltaic solar energy generation data collected at 15-min intervals.
2. Weather data collected from the Australian Bureau of Meteorology (BOM). This included Apparent Temperature, Air Temperature, Dew Point Temperature, Relative Humidity, Wind Speed and Wind Direction.  
#####

---
## Data Collection
   The dataset contains high-granularity solar energy generation data from 42 solar sites across five La Trobe University, Victoria, Australia campuses. The dataset includes nearly two years of solar energy generation data collected at 15-min intervals. 
  
   The weather data in the dataset was derived from the Australian Bureau of Meteorology (BOM) using the geographical placement of each campus. The weather data includes Apparent Temperature, Air Temperature, Dew Point Temperature, Relative Humidity, Wind Speed and Wind Direction.  

#####
---
## Data Cleaning
 The data provided was from 01-01-2020 at 6:45AM to 2022-04-23 at 17:15 (PM). This represents a timedelta of 843 days, 10 hours, and 30 min. The data was reindexed with a datetime index and separated by campus, ignoring the site location. This choice was made because longitude and latitude was recorded for each campus and the reported location of each site was reported as the larger campus location. The weather data would then match each campus, regardless of site number.  
 Next, the weather data was read in, reindexed as a datetime, and had significant missing data. It was then also split by campus number. The Solar Generation and Weather data were merged for each campus and exported.  
 To investigate the final model on a more granular scale, Campus 3 was split among its individual sites, and half the sites were exported to evaluated.

#####
---
## EDA
EDA was separated out by campus. But for each:
- the Daily Average Solar Generation across all the data was plotted to see the distribution of generation over time
- the non-zero generation data was viewed in boxplots to examine the power generation distribution
- the null values, shape, and duplicated indexes were calculated

Out of these different campuses, Campus 4 and 5's non-zero generation data was most normal and each only have one site at each campus. Randomly, Campus 5 was chosen to move forward with the modeling process.

############ distribution and avg daily for campus 5 here
summer and winter investigations too (subplots)

Next, the autocorrelation and partial autocorrelation plots were investigated for the 15-min frequency intervals.

#######plots here

The autocorrelation is very much like what was expected:
> Reflects the seasonality of night/day cycle - 48 lags (12 hours) cause the most negative score.
> 96 lags (equal to 1 day) is very highly correlated, but not quite 1
>> This is most likely due to differences in the weather

The partial autocorrelation shows the most important is the 15-min interval before the one in question. This absolutely makes sense due to the interval frequency in relation to solar-path interval.


The data was resampled for hourly and the autocorrelation and partial autocorrelation plots were investigated:

#######plots here

The autocorrelation and partial autocorrelation plots demonstrate the same things as the 15-min interval plots. However, the hourly partial autocorrelation also shows more importance in 2 lags as well as 21, 22, and 23 lags. 


Finally, four of eight sites at Campus 3 were examined and exported to determine if the Campus5 model can be applied more granularly at the site level. Specifically, Site 10 seems to have the most similar daily average plot as well as the same scale as Campus 5. Thus, Site 10 is the most likely site to be well modeled by the Campus 5 best model.


### Variance of fire data
![Scatter Plot](public/visuals/wildfire_all_size_vs_duration.png)
  
### Seasonality of precipitation and fires:
![Scatter Plot](public/visuals/fire_rain_snow.png)

### Most burned vegetation types:
![Scatter Plot](public/visuals/landcover_most_burned.png)


---
## Data Preprocessing

By examining the Solar Generation across the time span given, Campus 5 clearly shows broad seasonality (the actual Seasons - southern hemisphere's winter peaking around July and summer peaking around January) as well as 

----
## Modeling

### ARIMA Modeling

Initially, gridsearching ARIMA modeling was used on hourly-resampled data to try to get the best *p* and *q* hyperparameters (d was already established to be 0).

After running the ranged gridsearch, the best arima model was shown to be a ARIMA(10, 0, 7) model with an Akaike score of 38.0, which was excellent considering most ARIMA models were three orders of magnitude larger.

<kbd>![ResultImage](./images/arima_gridsearch.png)</kbd>

However, once plotted, this ARIMA model basically sinusoidally represents the daily seasonability with very low variance accounted for:


###@ Image
###@ Image

This resulted in MAE and RMSE scores of:

| Testing MAE |  Testing RMSE  |
| :---------: | :------------: |
|    1.472    |      1.873     |



### Lagged Modeling

Next, the lagged models of both the 15-min frequency data and the hourly sampled data were investigated. The number of lags were based on the partial autocorrelation determined in the EDA.

The 15-Min Freq Data:

###@ Image
###@ Image

Most of the preds look like the true values shifted over by 15 minutes. However, looking closely, especially at the second hundred intervals graphed (specifically around 9am on 11-10), the predictions and true values diverge briefly. This means the predictions aren't just relying on the first lagged value, even though that is the most utilitzed variable. The linear regression's coefficients proved this.


Lagged Linear Regression Scores

| Training R-Squared |  Testing R-Squared  |
| :----------------: | :-----------------: |
|       0.875        |        0.899        |

This shows the most informative lags still only account for 89.9% of the variability in the data. Therefore, things like the weather still play an important role in the variability.


Lagged Prediction Scores:

| Testing MAE |  Testing RMSE  |
| :---------: | :------------: |
|    0.260    |      0.629     |

These results demonstrates that a model that is updated every 15-min can predict the next 15-min interval with the above scores. However, modeling in that way would be very difficult to maintain. Thus, the RNN modeling's goal is to beat these scores.


### Recurrent Neural Network Modeling

 Using Google Colab, both Univariate and Multivariate modeling was investigated on the 15-min interval data, the resampled hourly data, and the resampled daily max data.

<u> Univariate Modeling:  </u>  
Exploring different combination of SimpleRNN and Dense layers, along with experiementing on different sequence lengths the two best models were found (best for MAE and best for RMSE).  

 Next, the best two models then had their Adam Optimizer's learning rate tuned to get the final, best model:

Best Model:
- 96 interval sequences (1 full day)
- SimpleRNN layer with 64 nodes
- Dense output layer (linear activation for Regression)
- Adam Learning Rate of 0.002

| Testing MAE |  Testing RMSE  |
| :---------: | :------------: |
|    0.1834   |     0.5831     |




<u> Multivariate Modeling:  </u>  

The weather data was incomplete compared to the solar generation data and was not included for the first year (approximately). So the dataframe was curtailed to where the weather data starts (index 33311). The weather was then interpolated using feed-forward methods, allowing for no missing data.

Next, the features were selected and scaled. Finally, the timeseries sequences were examined for 4 intervals (1 hour), 16 intervals (4 hours), and 96 intervals (1 day) and subsequently run through a variety of models, including LSTM, SimpleRNN and Dense layers.

The best model (4-hour sequences with LSTM and 96 nodes) gave results of:

| Testing MAE |  Testing RMSE  |
| :---------: | :------------: |
|   0.4346    |     0.8450     |

These scores are not nearly as optimal as those found through univartiate modeling. Thus, the top two univariate models will be used when investigating its application to entire campuses with many sites and to more granular, single sites within the larger campuses.


<u> Applying Best Models to Other Campuses and Sites:  </u>

Each of the other campuses (Campus 1-4) and four sites from Campus 3 (Sites 6, 8, 10, and 12) were used to train and test the two best models (and their respective sequence lengths) and the results are below:


![Scores](images/scores.png)

When compared to the results from Campus 5






######
###
####

   
     
### Distribution of True and Predicted Values:
![Histogram](public/visuals/True_vs_Preds.png)
     
     
     
I$$$$nvestigating the coefficients from the linear regression (2nd best model) showed the biggest factors it used was wind speed and surface soil wetness (5cm below). These findings makes sense within the context of our investigation. However, it was interesting present rain or past precipiation didn't affect the model as much as the other features.


----
## Conclusion & Recommendation

Based on the wide variety of analysis and modeling conducted, the best model could predict the solar generation output with a MAE score of less than 10% of the maximum solar generation output (0.6 kWh in the case of Campus 5).   

Moreover, the best model's architecture does reasonably well when applied to the other Campuses and the specific Sites examined (Sites 6, 8, 10, and 12 within Campus 3).   

However, the variability in the output relies on many things, such as the component's functionality and weather patterns. Consequently, future research on the weather data's effect on energy generation on these sites is recommended.

----

## Future Research




$$$$For future investigations, the model could potentially be better at predicting the size of the resulting fire by incorporating:
     
- Accurate Slope Data
- Geography - Human Elements such as roads which would allow quicker human intervention
- Geography - Natural Elements such as lakes, rivers, and steep mountains; giving a native boundary for the fire
- Narrowing the parameters for the investigation (i.e. - An area with only a certain vegetation coverage)

Also, it would be worth investigating modeling/predicting daily fire growth rather than total acres burned. This would allow the incorporation of weather data through the fire (i.e.- the second day might be extremely windy, allowing the fire to spread rapidly. This case would not have been accurately represented by our models in this study).


----



## Data Dictionary

| Features                | Data Types | Description                                                                                                                                                                                                                                                                                                         |
| :---------------------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Campus Key                     | Int    | Campus ID Key                                                                                                                                                                                                                   |
| Site Key                 | INT    | Site ID Key                                                                                                                                                                                                 |
| Timestamp                    | datetime    | datetime of the observation                                                                                                                                                                                                                  |
| SolarGeneration             | float64    | The kWh generated                                                                                                                                                                                     |
| ApparentTemperature                    | float64    | Apparent Temp (degrees C)                                                                                                                                                                                                                                  |
| AirTemperature                | float64    | Air Temp (degrees C)                                                                                                                                                                                                                                        |
| DewPointTemperature                    | float64    | Dew Point Temp (degrees C)                                                                                                                                                                                                                                  |
| RelativeHumidity                | float64    | Humidity Percentage                                                                                                                                                                                                                                        |
| WindSpeed                    | float64    | Windspeed (m/s)                                                                                                                                                                                                                                  |
| WindDirection                | float64    | Wind Direction (degrees from North)                                                                                                                                                                                                                                        |
