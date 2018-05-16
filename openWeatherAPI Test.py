'''
Using PyOWM to pull from API.

PyOWM is a client Python wrapper library for the OpenWeatherMap (OWM) web API.

It allows quick and easy consumption of OWM weather data from Python applications via a simple object model and in a human-friendly fashion.

https://github.com/csparpa/pyowm

install using

$ pip install pyowm


Using this module so I do not have to worry about maintaing the API connection.

Ran into issues with Visual Studio not reconizing the Module was installed and only opening in Visual Studio.

Ways to imporove:

Add in tests for valid city, no numbers, only str/english characters are entered
'''


city_name = input("What city would you like the weather for?") # use prompt to get city name and store in city_name

def apiCall(city_name):

    import pyowm #imports pyOWM'
    owm = pyowm.OWM('1530b5062d6129f35937dbb26cc05fbe') #sets my API Key'
    observation = owm.weather_at_place(city_name) #using pyowm to pull weather for city_name'
    w = observation.get_weather() #sets the pulled weather as w'
    tempCDict = w.get_temperature('celsius') #Dictionary of Temp in C
    tempC= " in degrees Celsius is " + str((tempCDict).get('temp')) #adding a message and temp in Celsius

    tempFDict = w.get_temperature('fahrenheit') #Dictionary of Temp in F
    tempF= " and in degrees Fahrenheit is " + str((tempFDict).get('temp')) #adding a message and temp in Fahrenheit

    windSpeedDict = w.get_wind() #Dictionary of Wind Speed
    windSpeed =" while the wind speed in MPH is " + str((windSpeedDict).get('speed')) #adding a message and wind speed

    weatherStr = "The temperature for " + city_name + tempC  + tempF  + windSpeed #combining what I want to display with the temp and wind to be printed
    return (weatherStr)


print(apiCall(city_name))

