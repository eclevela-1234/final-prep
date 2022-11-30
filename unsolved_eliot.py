'''
Weather Finder
===============
The code should retrieve the current weather of each city listed in the provided csv file using the OpenWeatherMap API.
It should then print a running list of JSONs for each city in the console.
It should finally save the city names and temperatures in a new csv.

'''

# Dependencies
import requests as req
# import json
import csv

# OpenWeather API Key
api_key = "417bfe8effcb6b9aa355a4de24d62458"

# Specify File Path
csvpath = "cities.csv"


# Read CSV
with open(csvpath) as csvfile:

    # Read the file specifying commas as delimiters
    csvreader = csv.reader(csvfile, delimiter=",")

    # Iterate through each row of the CSV
    for row in csvreader:

        # Print each row of the csv
        print(row[0])
        city = row[0]

        # Build an endpoint URL to the OpenWeatherMap Service
        url = "http://api.openweathermap.org/data/2.5/weather?"
        query_url = url + "q=" + city + "&appid=" + api_key+ "&units=Imperial"

        print(query_url)
        # Make a request to the endpoint url
        weather_response = req.get(query_url)
        weather_json = weather_response.json()

        # Print the JSON for each
        print(weather_json)

        # # Extract the temperature for each city
        temperature = weather_json["main"]["temp"]

        # # Print the Temperatures
        print(temperature)


        # Draw a separating line
        print("---------------")

        # Write the contents for each to a new CSV
        output_file = "output.csv"
        with open(output_file, "a", newline='') as csvfile:

            # Initialize the csv.writer
            csvwriter = csv.writer(csvfile, delimiter=",")

            # Write each row
            csvwriter.writerow([row[0], temperature])



