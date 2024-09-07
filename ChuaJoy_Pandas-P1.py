#Import pandas libraru
import pandas as df

#Load the corresponding .csv file into a data frame named cars using pandas
cars = df.read_csv('cars.csv')

#Display first 5 rows
cars.head()

#Display last 5 rows
cars.tail()