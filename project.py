print "Hello! Welcome to Cheapest Flights around the World!"

import urllib2
import json

origin = raw_input ("Origin of destination ").upper()
destination = raw_input ("Final destination ").upper()
departure_day = raw_input ("Departure day (yyyy-mm-day) ")
adult_passengers = raw_input ("How many adults are traveling? ")


url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCA9UXD4NP9oAOkA4I0WyHmoC-Q2HFCXyU"
code = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": adult_passengers,
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": origin,
        "destination": destination,
        "date": departure_day,
      }
    ],
    # "refundable": false,
    "solutions": 20
  }
}
jsonreq = json.dumps(code, encoding = 'utf-8')
req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
# print req
# print dir(req) 
flight = urllib2.urlopen(req)
response = flight.read()
flight.close()
# print(response)

FareFlights = json.loads(response) #turns json into a dictionary


FlightFares = FareFlights['trips']["tripOption"][0]["saleTotal"]
# Departure = FareFlights['trips']["tripOption"][0]["saleTotal"]['slice'][2]['leg'][2]['departureTime']
Departure_Time = FareFlights['trips']["tripOption"][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
Arrival_Time = FareFlights['trips']["tripOption"][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']

# # Arrival = FareFlights['trips']["tripOption"][0]["saleTotal"]

# 
# Carrier = FareFlights['trips']["data"][0]["carrier"][0]['name']
# Aircraft = FareFlights['trips']["data"][0]["aircraft"][0]['name']


print FlightFares
print Departure_Time
print Arrival_Time
# print Carrier
# print Aircraft

# for keys, value 


#  primary_colors = ('red', 'yellow', 'blue')

# print primary_colors[-1]

# print FlightFares = []
# for saleTotal in response:
#   for keys, value in film.items():
#       if "fun_fact" in keys:
#           movie_film_fact = film['title'] + ": " + value
#           if movie_film_fact not in film_fact_list:
#               film_fact_list.append(movie_film_fact)

