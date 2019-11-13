#!/usr/bin/env python

import pandas as pd

def get_dfs():
    df_brazil= pd.read_csv("sudeste.csv",skipinitialspace=True,usecols=["temp","date"])
    df_madrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv",skipinitialspace=True,usecols=["Mean TemperatureC","CET"])
    return df_brazil,df_madrid

df_brazil,df_madrid = get_dfs()

def transform(brazil,madrid):
    madrid.rename(columns={"CET":"date","Mean TemperatureC":"temp-madrid"},inplace=True)
    brazil = brazil.groupby("date",as_index=False).mean()
    final = madrid.merge(df_brazil,how='inner',on=["date"])
    final.rename(columns = {"temp":"temp-brazil"})
    return final

df_final = transform(df_brazil,df_madrid)
print("Correlation")
print(df_final.corr(method='pearson'))

# Interpretation of results #
# Correlation coefficient = -0.00207 indicates a weak negative
# linear relationship, which means when Madrid's daily tempature changes,
# Brazil's daily tempature tends to change in slighlty oppsite direction.
# Yet, we can easily interpret that when Madrid's tempature increases,
# there is no tendency for the Brazil's tempature to change in a specific
# direction since correlation coefficient is almost zero.
# Doğaç Çakır, 2148781


