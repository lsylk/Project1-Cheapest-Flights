print "Hello! Welcome to Cheapest Flights around the World!"

import urllib2
import json

print "Please enter the airport code for origin or destination, i.e. LAX"
origin = raw_input ("Origin of destination ").upper()
destination = raw_input ("Final destination ").upper()
departure_day = raw_input ("Departure day (yyyy-mm-day) ")
adult_passengers = raw_input ("How many adults are traveling? ")
nosolutions = raw_input ("How options do you want? ")

url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=XXXX"
code = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": int(adult_passengers),
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": origin,
        "destination": destination,
        "date": departure_day,
      }
    ],
    "solutions": int(nosolutions)
  }
}
jsonreq = json.dumps(code, encoding = 'utf-8')

req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})

flight = urllib2.urlopen(req)

response = flight.read()
flight.close()

FareFlights = json.loads(response) #turns json into a dictionary


Answerlist=[]
for i in range(int(nosolutions)):
  FlightFares = FareFlights['trips']["tripOption"][i]["saleTotal"]
  Departure_Time = FareFlights['trips']["tripOption"][i]['slice'][0]['segment'][0]['leg'][0]['departureTime']
  Arrival_Time = FareFlights['trips']["tripOption"][i]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
  Carrier = FareFlights['trips']["tripOption"][i]['slice'][0]['segment'][0]['flight']['carrier']
  Aircraft = FareFlights['trips']["tripOption"][i]['slice'][0]['segment'][0]['leg'][0]['aircraft']

  Answer = "Price: " + FlightFares + "  Departure Time: " + Departure_Time + "  Arrival Time: " + Arrival_Time + "  Airline: " + Carrier + "  Aircraft: " + Aircraft
  Answerlist.append(Answer)
  print Answerlist[i]


