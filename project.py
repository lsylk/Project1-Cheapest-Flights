apiURL = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyDactDzfEYQuhLWXXbCm85A4GkVsrXopDQ"

# print "Hello! Welcome to Cheapest Flights around the World!"

# origin = raw_input ("Origin of destination ")
# destination = raw_input ("Final destination ")
# departure_day = raw_input ("Departure day ")
# arrival_day = raw_input ("Arrival day ")
# adult_passengers = raw_input ("How many adults are traveling? ")


# apiURL = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyDactDzfEYQuhLWXXbCm85A4GkVsrXopDQ"

# response = urlopen(apiUrl)

        
  
# print response

{
  "request": {
    "slice": [
      {
        "origin": "SFO",
        "destination": "LAX",
        "date": "2016-03-25"
      },
      {
        "origin": "SFO",
        "destination": "SAN",
        "date": "2016-03-25"
      }
    ],
    "passengers": {
      "adultCount": 1,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 0,
      "seniorCount": 0
    },
    "solutions": 20,
    "refundable": false
  }
}