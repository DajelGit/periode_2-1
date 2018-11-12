'''
statistics.minutes delayed.weather: number of minutes delayed (per month) caused by significant meteorological
conditions that, in the judgment of the carrier, delays or prevents the operation of a flight.

a) maak een lijst van tuples (code_airport, minutes_delayed_weather)
b) sorteer deze lijst op minutes_delayed_weather en print de paren (code_airport minutes_delayed_weather)
'''

import json
from pprint import pprint

list_of_airports = []

with open('airports.json', 'r') as infile:
    airport_list = json.load(infile)
    # pprint(list_of_airports)

for airport in airport_list:
    code = airport['airport']['code']
    min_delayed_weather = airport['statistics']['minutes delayed']['weather']
    list_of_airports.append((code, min_delayed_weather))

for e in list_of_airports:
    print(e)

#sort airports by min_delayed_weather
my_sorted_list = sorted(list_of_airports, key=lambda k: k[1], reverse=True)
for x,y in my_sorted_list:
    print(x,y)

