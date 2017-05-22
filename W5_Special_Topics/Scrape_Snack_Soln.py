import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

#Don't forget to start mongo daemon!!
# in mongo shell:
#   use scrapey_scrapey
#   db.createCollection('snacky_snacky')
client = MongoClient()
database = client['all_da_snacks']
coll = database['yum']

#Get our base URL for the site we are scraping
url = "http://www.snackdata.com"
req = requests.get(url)

#Parse the returned string as html using BS4:
soup = BeautifulSoup(req.text, 'html.parser')

# All of our snacks we want are listed inside an ordered list tag
# Use select to get all li inside an ol
list_items = soup.select("ol li")

# step through each food item and get its href link so we can loop through each snack and collect its data we want
links = []
for li in list_items:
    links.append(li.a['href'])

#Now loop through each snack:
for link in links:
    url_snack = url + link
    req_snack = requests.get(url_snack)
    soup_snack = BeautifulSoup(req_snack.text, 'html.parser')

    #The Snack name and number are both in an h4 tag, but it has a weird unicode 'No.' char that we have to strip out:
    name_number = soup_snack.select('h4')[0].text.encode("ascii", "ignore")
    snack_number = name_number.split()[0]
    snack_name = ' '.join(name_number.split()[1:])

    #flavor, cuisine, series, and components are all sitting in a table with dd tags for each line insode the dl (definition list) tags.
    tab = soup_snack.find_all('div', attrs={"class": "data clearfix"})
    tab_dd = tab[0].find_all('dd')
    flavor = tab_dd[0].text.strip().split(',')
    cuisine = tab_dd[1].text.strip()
    series = tab_dd[2].text.strip().split(',')

    comp_list = tab_dd[3].select('img')
    comps = []
    for comp in comp_list:
        comps.append(comp.get('alt', ''))


    #Date, description, and taste are all inside the text inside a div with id 'rightstuff', so we can just split on \n and grab the paragraph we need:
    full_txt = soup_snack.find_all('div', attrs={'id': 'rightstuff'})[0].text.split('\n')
    date = ' '.join(full_txt[6].split()[-3:])

    descr = full_txt[3]
    taste = re.sub('Taste', '',full_txt[4])

    #Now for the fun Mongo mania:
    coll.insert_one({'name': snack_name,
                    'number': snack_number,
                    'flavor': flavor,
                    'cuisine': cuisine,
                    'series': series,
                    'composition': comps,
                    'date_added': date,
                    'description': descr,
                    'taste': taste
                    })
