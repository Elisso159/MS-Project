import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

datetime_col = ["pickup_datetime" , "dropoff_datetime" , ]
def format2_timestamp(df : pd.DataFrame)->pd.DataFrame :
    df = df.copy()
    for feature in datetime_col :
        df[feature] = pd.to_datetime(df[feature] , format="%Y-%m-%d %H:%M:%S")
    return df

def remov_non_valid_trips(df : pd.DataFrame ,features : list[str]) ->pd.DataFrame:
    return df[(df[features[0]] > 0) & (df[features[1]] > 0)].copy()
    
df = pd.read_csv("train.csv" , keep_default_na=False).copy()
df =format2_timestamp(df)
df = remov_non_valid_trips(df, ["passenger_count" , "trip_duration"])

    

