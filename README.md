simple_yahoo_weather
=============

A Simple Yahoo API Wrapper for Python3
-------------

The goal of this API wrapper is to be as easy to use as possible. Given both a unit and a Yahoo WOEID it will return a dictionary sorted by day of all relevant information given by the Yahoo API

**Installation**

Simply drag and drop the yahoo_weather folder into your working python directory. 

Too add to your code:

    from yahoo_weather import yahoo_weather

Example:

     from yahoo_weather import yahoo_weather #Import yahoo_weather module
     yw = yahoo_weather.YWeather() #Shorten class name 
     data = yw.weather_data(6, 'c') #Call the weather function (WOEID, unit)

Output:

     >>> data['day0']['high']
     >>> '5'
     
     >>> data['day3']
     >>> {'high': '9', 'code': '11', 'low': '-1', 'date': '8 Apr 2014', 'text': 'Showers', 'conditions': 'showers', 'day': 'Tue'}
     
     >>> data['day3']['conditions']
     >>> 'showers'
     

Documentation
------------

    yahoo_weather.YWeather().weather_data(WOEID, UNIT)
  This function returns all useful information given by the Yahoo weather API for a given WOEID. It returns a dictionary type object. It is formatted by day, where TODAY is day0 and the fifth and final day is day4.
  
Format of dictionary:

     ['pubDate', 'language', 'day2', 'day3', 'day0', 'day1', 'location', 'location_long', 'units', 'yahoo_link', 'location_lat']
     
     pubDate - The time/day yahoo updated weather data
     language - The language yahoo is using, generally english
     dayX - All weather data, expanded below
     location - A dictionary containing the city, province (or state), and country
     location_long - The longitudial coordinate of the WOEID
     location_lat - The Latitudial coordinate of the WOEID
     units - Dictionary of units used for various weather related data (distance, temperature, pressure)
     yahoo_link - A link to the relevant Yahoo Weather page

DayX format:

    Day0 had a special format as it both includes forecast and current weather information:
    ['atmosphere', 'code', 'text', 'current_conditions', 'high', 'date', 'astronomy', 'day', 'low', 'wind']
    The rest are the same except they exclude current_conditions, atmosphere, astronomy, and wind for obvious reasons
    
    atmosphere - Current atmospheric conditions (pressure, rising, visibility, humidity)
    current_conditions - Dictionary of current weather conditions (date, text (conditions), temperature)
    astronomy - Dictionary of time of sunrise and sunset
    wind - Dictionary 
    
    text - Weather conditions (sunny, rainy, etc)
    code - A specific code Yahoo uses to generate the 'text' key above (mostly useless information)
    The rest are obvious
    
    
