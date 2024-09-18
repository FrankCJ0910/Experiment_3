Both probelms will be using the Pandas library
Using this line, imported pandas as df

``` python
  import pandas as df
```

First thing to do was load in the given csv file. Using .read_csv loaded given file into variable cars

``` python
  cars = df.read_csv('cars.csv')
```

Problem 1 tasked us to find the first and last 5 rows of cars. So we use .head() and .tail() functions to display them

```python
  cars.head()
  cars.tail()
```

Problem 2 tasks us to find and display different parts of the dataframe. First asks to display first 5 rows and display every odd column. So iloc is used

``` python
  cars.iloc[0:5,1::2]
```

Next is to find a specific model of car and display its stats so use .loc

``` python
  cars.loc[cars['Model']=='Mazda RX4']
```

Next is to find another specific model but only display its cyclinder count so same as before but add another parameter to only display cyclinder count

``` python
  cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
```

Last asks to find multiple models so first create a list of models to be displayed. Then in the parameters in .loc use isin instead of == then place the list for easier usability then add another set of parameters to display only the columns needed

``` python
  car_models = ['Camaro Z28', 'Ford Pantera L', 'Honda Civic']
  cars.loc[cars['Model'].isin(car_models),['Model','cyl','gear']]
```
