def testWeather():
	assert apiCall(Iowa City) == "The temperature for Iowa City in degrees Celsius is 27.2 and is in degrees Fahrenheit 80.96 while the wind speed in MPH is 2.1"
	assert apiCall(London) == "The temperature for London in degrees Celsius is 8.33 and in degrees Fahrenheit is 46.99 while the wind speed in MPH is 4.6"
	
	
def testWeatherSelf(self):	
	assert apiCall(self) == "The temperature for self in degrees Celsius is 8.33 and in degrees Fahrenheit is 46.99 while the wind speed in MPH is 4.6"