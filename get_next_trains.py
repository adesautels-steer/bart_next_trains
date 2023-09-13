import os
import requests

# prompt for origin and destination stations
station_orig = input("Please enter the origin station code.\n")
station_dest = input("\nPlease enter the destination station code.\n")

# assemble API parameters
api_key = os.environ.get("BART_API_KEY")
payload = {
    "cmd": "depart",
    "orig": station_orig,
    "dest": station_dest,
    "date": "now",
    "b": 0,
    "a": 3,
    "key": api_key,
    "json": "y",
}

# call API and parse response
r = requests.get("https://api.bart.gov/api/sched.aspx", params=payload)
trips = r.json()["root"]["schedule"]["request"]["trip"]

# print out formatted trip information
print(f"\nNext trips between {station_orig} and {station_dest}:")
i = 1
for trip in trips:
    print(
        f"Option {i}: departs {station_orig} at {trip['@origTimeMin']} and "
        f"arrives {station_dest} at {trip['@destTimeMin']} "
        f"({trip['@tripTime']} minutes, ${trip['@fare']})."
    )
    i += 1
print()
