import json
import requests

#Send a GET request to the latest launch endpoint, dump the json to text and then load in as a dictionary
latest_launch_response = requests.get("https://api.spacexdata.com/v5/launches/latest")
latest_launch_text = json.dumps(latest_launch_response.json(),sort_keys=True,indent=4)
print(latest_launch_text)
latest_launch = json.loads(latest_launch_text)

#Set relevant ID variables from the latest launch dictionary.  Designed to be used as params for a later GET query
rocket_params = {'id':latest_launch['rocket']}
crew_id = latest_launch['crew']
launchpad_id = latest_launch['launchpad']
ships_id = latest_launch['ships']

#Send a GET request to the individual rocket endpoint with parameters of the rocket ID from the latest launch
rocket_response = requests.get("https://api.spacexdata.com/v4/rockets/",params=rocket_params)

#Print the response from the GET request.  This is because I spent hours receiving 404 errors, eventually discovering that I'd copied the URL from the endpoint Docs directly (the ":id" needed removing from the end).
print(rocket_response)

#Annoyingly the dump and load this time returns a list of dictionaries, making it difficult to pick out the name.  I'm sure given time I could code up the right index and then call from the relevant dictionary but it took me so long to correct the 404 error that I didn't get that far.
rocket_text = json.dumps(rocket_response.json(),sort_keys=True,indent=4)
rocket = json.loads(rocket_text)
print(rocket)


#All in all I suspected as I was doing it this way that there was a more concise way to write a query that pulls everything through into a single dictionary before pretty printing it but I couldn't wrap my head around how.  The method I started with seems unnecessarily complicated and time consuming.