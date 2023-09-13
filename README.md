# Next Bart Trains

This program prompts the user to enter origin and destination BART station
codes, and returns schedule and fare details from the [BART Legacy API](https://www.bart.gov/schedules/developers/api) for the next three possible trips
between the selected stations.

## Setup and Usage

1. Create and activate a virtual environment (optional, but recommended)
   1. `python -m venv venv`
   2. `. venv/Scripts/activate` 
2. Install required packages `python -m pip install -r requirements.txt`
3. Export Bart API key environment variable with `export BART_API_KEY=[YOUR_API_KEY]`
4. Run with `python next_bart_trains.py`

## Notes

BART station codes are available [here](https://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V&json=y).

## Contact

Please contact [Andrew Desautels](mailto:andrew.desautels@steergroup.com) with any questions.