import requests
import json
from pprint import pprint

if __name__ == '__main__':

#39.734423,-104.930639 my is test property location on VRBO
options = dict(
    page_no = 1,
    checkin = "06/04/2017",
    checkout = "06/07/2017",
    sw_lat = "39.732423",
    sw_lng = "-104.950639",
    ne_lat = "39.736423",
    ne_lng = "-104.910639"
)

json_url = "https://www.airbnb.com/search/search_results?page={page_no}&source=map&airbnb_plus_only=false&\
sw_lat={sw_lat}&sw_lng={sw_lng}&ne_lat={ne_lat}&ne_lng={ne_lng}&search_by_map=true&location=Denver,+CO,+United+States\
&checkin={checkin}&checkout={checkout}&guests=1".format(**options)

raw = requests.get(json_url).text
data = json.loads(raw)

# listing
# pprint( data['results_json']['search_results'][0]['listing'])
# price info
# pprint( data['results_json']['search_results'][0]['pricing_quote'])

hits = data['results_json']['search_results']
for prop in range(len(hits)):
    listing = hits[prop]['listing']
    print('\n---- Name: {}, Lat: {}, Lng: {}.----\n'.format(listing['name'], listing['lat'], listing['lng']))
    print(listing)
