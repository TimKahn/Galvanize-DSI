import requests
import os
import json
import pandas as pd
from pprint import pprint
from geopy.geocoders import GoogleV3

def get_url():

    url1 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.70476766058143,-104.93988983081056,39.75803614055964,-104.90727416918946,14z?swLat=39.70476766058143&swLong=-104.93988983081056&neLat=39.75803614055964&neLong=-104.90727416918946&zoom=14&page=1&region=2332&from-date=2017-05-25&to-date=2017-05-26&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&sleeps=1-plus&_=1495661060970'

    url2 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.70806925814718,-104.93997566149903,39.761335187806544,-104.90735999987794,14z?swLat=39.70806925814718&swLong=-104.93997566149903&neLat=39.761335187806544&neLong=-104.90735999987794&zoom=14&page=1&region=2332&from-date=2017-05-25&to-date=2017-05-26&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&sleeps=1-plus&_=1495661060971'

    url3 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.710924687732216,-104.9412634742871,39.75778838099063,-104.908647812666,14z?swLat=39.710924687732216&swLong=-104.9412634742871&neLat=39.75778838099063&neLong=-104.908647812666&zoom=14&page=1&region=2332&from-date=2017-06-04&to-date=2017-06-07&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&_=1495798487734'

    url4 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.65237457610901,-105.04965595142579,39.826878836475025,-104.93086627857423,12z?swLat=39.65237457610901&swLong=-105.04965595142579&neLat=39.826878836475025&neLong=-104.93086627857423&zoom=12&page=1&region=2332&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&sleeps=1-plus&_=1496211019307'

    return url4

def get_data(json_url):
    raw = requests.get(json_url).text
    data = json.loads(raw)
    return data['results']['hits']

def rev_geo(lat, lon):
    location = geolocator.reverse((lat, lon))
    address_info = str(location[0]).split(',')
    print(address_info)
    address = address_info[0]
    zipcode = address_info[2].split()[1]
    return address, zipcode

def get_properties(hits):
    properties = []
    for prop in range(len(hits)):
        p = hits[prop]
        geo = p['geoCode']
        if geo['exact'] == True:
            lat, lon = geo['latitude'], geo['longitude']
            address, zipcode = rev_geo(lat, lon)
            properties.append([int(p['listingNumber']), p['headline'].strip(), lat, lon, address, zipcode])
    return pd.DataFrame(properties, columns = ['listingNumber', 'headline', 'lat', 'lon', 'address', 'zipcode'])

if __name__ == '__main__':
    geolocator = GoogleV3(api_key=os.environ['GMAPS_GEOLOCATOR'])
    url = get_url()
    hits = get_data(url)
    properties = get_properties(hits)
