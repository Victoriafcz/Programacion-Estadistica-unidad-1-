
import pandas as pd

dataframe = pd.read_csv("aircraft_dataset.csv")

print(dataframe)

print(dataframe["Cargo Capacity (kg)"].min())
print(dataframe["Cargo Capacity (kg)"].median())
print(dataframe["Cargo Capacity (kg)"].max())
print(dataframe[dataframe["Center of Gravity limits"]>.025])
