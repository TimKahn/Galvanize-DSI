import requests
import json
from pprint import pprint

def get_url():
    '''
    url1 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.70476766058143,-104.93988983081056,39.75803614055964,-104.90727416918946,14z?swLat=39.70476766058143&swLong=-104.93988983081056&neLat=39.75803614055964&neLong=-104.90727416918946&zoom=14&page=1&region=2332&from-date=2017-05-25&to-date=2017-05-26&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&sleeps=1-plus&_=1495661060970'

    url2 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.70806925814718,-104.93997566149903,39.761335187806544,-104.90735999987794,14z?swLat=39.70806925814718&swLong=-104.93997566149903&neLat=39.761335187806544&neLong=-104.90735999987794&zoom=14&page=1&region=2332&from-date=2017-05-25&to-date=2017-05-26&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&sleeps=1-plus&_=1495661060971'
    '''

    url3 = 'https://www.vrbo.com/ajax/map/results/vacation-rentals/@39.710924687732216,-104.9412634742871,39.75778838099063,-104.908647812666,14z?swLat=39.710924687732216&swLong=-104.9412634742871&neLat=39.75778838099063&neLong=-104.908647812666&zoom=14&page=1&region=2332&from-date=2017-06-04&to-date=2017-06-07&searchTermContext=9b810827-b5cb-4e59-a1f0-553027e04694&searchTermUuid=9b810827-b5cb-4e59-a1f0-553027e04694&_=1495798487734'

    return url3

if __name__ == '__main__':
    json_url = get_url()
    raw = requests.get(json_url).text
    data = json.loads(raw)
    results = data['results']
    hits = results['hits']
    for prop in range(len(hits)):
        print('\n---- {} ----\n'.format(hits[prop]['headline']))
        print(hits[prop]['geography'])
        #pprint(hits[prop])
