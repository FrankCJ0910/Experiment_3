#Import pandas libraru
import pandas as df

#Load the corresponding .csv file into a data frame named cars using pandas
cars = df.read_csv('cars.csv')

#Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars.iloc[0:5,1::2]

#Display the row that contains the ‘Model’ of ‘Mazda RX4’.
cars.loc[cars['Model']=='Mazda RX4']

#How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]

#Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
car_models = ['Camaro Z28', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(car_models),['Model','cyl','gear']]