# Forecasting the Citi Bike demand in NYC [in progress]

**Introduction**

New York's bike-sharing program, Citi Bike, is the largest in the United States. It has over 14,000 bikes and 900 stations across Manhattan, Brooklyn, Queens, and Jersey City. 
Has a daily rider, I am curious to see how closely forecasting methods can get to the actual numbers and how different forecasting methods compare on this dataset.


**Dataset** 

The data is available on the [Citi Bike System Data](https://www.citibikenyc.com/system-data) website. The data is available in the form of CSV files for each month from 2013 to 2023. 
The data contains the following columns:
- Trip Duration (seconds)
- Start Time and Date
- Stop Time and Date
- Start Station Name
- End Station Name
- Station ID
- Station Lat/Long
- Bike ID
among others.

In the project I start by working with aggregated data at the daily level. I aggregate the data to the daily level and get 
the total number of trips for each day. 

**Objective**

I use the aggregated data to forecast the demand for Citi Bike in NYC. 
The goal is to benchmark the following forecasting methods on this dataset:
- Sarima : there is of course a strong seasonality in the data.
- LSTM : a type of recurrent neural network that is well-suited to time series data.
- Autoformer : a transformer-based model that is designed for time series forecasting.

Another objective is to get familiar with the GluonTS and Hugging Face libraries to implement the Autoformer.


