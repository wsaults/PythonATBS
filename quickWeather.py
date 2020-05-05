#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint

# Compute location from command line arguments.
if len(sys.argv) < 2:
  print('Usage: quickWeather.py loction')
  sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=63a7a37aaacf05a109e77797f3af426d' % (location)
response = requests.get(url)

# Load JSON data into Python variable
weatherData = json.loads(response.text)
pprint.pprint(weatherData)

# Print weather descriptions.
w = weatherData['list']

today = w[0]
tomorrow = w[1]
dayAfter = w[2]
w0 = today['weather'][0]
t0 = today['temp']
w1 = tomorrow['weather'][0]
t1 = tomorrow['temp']
w2 = dayAfter['weather'][0]
t2 = dayAfter['temp']

print('\nCurrent weather in %s:' % (location))
print(w0['main'], '-', w0['description'])
print('High -', t0['max'])

print('\nTomorrow:')
print(w1['main'], '-', w1['description'])
print('High -', t1['max'])

print('\nDay after tomorrow:')
print(w2['main'], '-', w2['description'])
print('High -', t2['max'])