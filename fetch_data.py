import requests
import json
from datetime import date, timedelta
from tenacity import retry, stop_after_attempt, wait_exponential
import logging


logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def fetch_earthquake_data():

    month_ago = (date.today() - timedelta(days=1)).isoformat()
    todays_date = date.today().isoformat()

    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={month_ago}&endtime={todays_date}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise
    

# RETURN EXAMPLE BELOW

# {
#     "type": "Feature",
#     "properties": {
#         "mag": 0.68,
#         "place": "2 km WNW of Loma Linda, CA",
#         "time": 1772759180670,
#         "updated": 1772824871726,
#         "tz": null,
#         "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci41198295",
#         "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci41198295&format=geojson",
#         "felt": null,
#         "cdi": null,
#         "mmi": null,
#         "alert": null,
#         "status": "reviewed",
#         "tsunami": 0,
#         "sig": 7,
#         "net": "ci",
#         "code": "41198295",
#         "ids": ",ci41198295,",
#         "sources": ",ci,",
#         "types": ",nearby-cities,origin,phase-data,scitech-link,",
#         "nst": 31,
#         "dmin": 0.07686,
#         "rms": 0.14,
#         "gap": 64,
#         "magType": "ml",
#         "type": "earthquake",
#         "title": "M 0.7 - 2 km WNW of Loma Linda, CA"
#     },
#     "geometry": {
#         "type": "Point",
#         "coordinates": [
#             -117.279333333333,
#             34.0526666666667,
#             16.83
#         ]
#     },
#     "id": "ci41198295"
# }

