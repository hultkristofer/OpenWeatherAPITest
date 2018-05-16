'''
Using PyOWM to pull from API.

PyOWM is a client Python wrapper library for the OpenWeatherMap (OWM) web API.

It allows quick and easy consumption of OWM weather data from Python applications via a simple object model and in a human-friendly fashion.

https://github.com/csparpa/pyowm


$ pip install pyowm
'''


city_name = input("What city would you like the weather for?") # use prompt to get city name and store in city_name

def apiCall(city_name):

    import pyowm #imports pyOWM'
    owm = pyowm.OWM('1530b5062d6129f35937dbb26cc05fbe') #sets my API Key'
    observation = owm.weather_at_place(city_name) #using pyowm to pull weather for city_name'
    w = observation.get_weather() #sets the pulled weather as w'
    tempC= "is degrees Celsius" + w.get_temperature('celsius') #adding a message and temp in Celsius
    tempF= "and degrees Fahrenheit" + w.get_temperature('fahrenheit') #adding a message and temp in Fahrenheit
    windSpeed ="while the wind speed is" + w.get_wind() #adding a message and wind speed

    weatherStr = "Weather for" + city_name + tempC  + tempF  + windSpeed #combining what I want to display with the temp and wind to be printed
    return (weatherStr)


print(apiCall(city_name))
