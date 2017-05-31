import pandas as pd
import numpy as np
from numpy import nan
from airdna_db import airdna_query,airdna_update,airdna_query_raw
import string
from math import radians, cos, sin, asin, sqrt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from whoswho import who
import multiprocessing
import pdb
import time
import webbrowser


# query_text = '''
#
# SELECT * FROM region WHERE type LIKE 'zipcode'
# '''
#
# current_df = airdna_query(query_text)

# df.to_csv('../data/lyon_hosts.csv',sep=',',encoding='utf-8',quoting=True)

# attom_df = pd.read_csv('../data/attom_home_values.csv')
# attom_df.rename(columns=lambda x: '_'.join(x.replace('-','').lower().split()), inplace=True)
# attom_df = attom_df[attom_df['zipcode']>76000]
#
# for z in attom_df.iterrows():
#     zipcode = z[1][0]
#
#     print '----{}----'.format(zipcode)
#     query_text = '''
#     select *
#     from region
#     where type like 'zipcode'
#     and name::int=%s
#     ''' % zipcode
#
#     db_row = airdna_query(query_text)
#
#     data = z[1].values
#     cols = ['z_price_sqft','z_hvi_all','z_hvi_1bdrm','z_hvi_2bdrm','z_hvi_3bdrm','z_hvi_4bdrm','z_hvi_5bdrm']
#
#     lst = zip(cols,data[3:])
#     h = pd.DataFrame(lst)
#     h.dropna(inplace=True)
#     new = [tuple(x) for x in h.values]
#
#     fields = ['='.join([i[0],str(i[1])]) for i in new]
#     fields = ','.join(fields)
#
#     if db_row.shape[0]>0 and len(fields)>0:
#         db_row =  db_row[['z_price_sqft','z_hvi_all','z_hvi_1bdrm','z_hvi_2bdrm','z_hvi_3bdrm','z_hvi_4bdrm','z_hvi_5bdrm']]
#
#
#         update_text = '''
#         update region
#         set {}
#         where name::int=%s
#         and type='zipcode'
#
#         ''' % zipcode
#
#         update_text = update_text.format(fields)
#
#         # print db_row
#         # print update_text
#
#         airdna_update(update_text)

#
# print 'Loading first...'
#
# pth = '../../AIRDNA_RECORDER_0001/AIRDNA_RECORDER_0001.txt'
#
# lst = []
# with open(pth,'r') as f:
#     first_line = f.readline()
#     cols = first_line.strip().split('||')
#     for line in f:
#         line = line.strip().split('||')
#         lst.append(line)
#
# df1 = pd.DataFrame(lst,columns = cols)
#
# print 'Full load done ...'
#
# cols_1 = ['[ATTOM ID]','DocumentRecordingStateCode','DocumentRecordingCountyName','Grantee1NameFull','Grantee2NameFull','Grantee3NameFull','PropertyAddressFull','PropertyAddressCity','PropertyAddressState','PropertyAddressZIP']
#
# df1 = df1[cols_1]
#
# print 'Done!'
#
# print 'Loading second...'
#
pth = '../../AIRDNA_TAXASSESSOR_0001/AIRDNA_TAXASSESSOR_0001.txt'

lst = []
with open(pth,'r') as f:
    first_line = f.readline()
    cols = first_line.strip().split('||')
    for line in f:
        line = line.strip().split('||')
        lst.append(line)

df2 = pd.DataFrame(lst,columns = cols)

print 'Full load done ...'
#
# cols_2 = ['[ATTOM ID]','SitusStateCode','SitusCounty','MSAName','NeighborhoodCode','PropertyAddressFull','PropertyAddressCity','PropertyAddressState','PropertyAddressZIP','PropertyLatitude','PropertyLongitude',
# 'PartyOwner1NameFull',
# 'PartyOwner2NameFull',
# 'PartyOwner3NameFull',
# 'DeedOwner1NameFull',
# 'DeedOwner2NameFull',
# 'DeedOwner3NameFull',
# 'DeedOwner4NameFull',
# 'PartyOwner1NameFirst',
# 'PartyOwner2NameFirst',
# 'PartyOwner3NameFirst',
# 'DeedOwner1NameFirst',
# 'DeedOwner2NameFirst',
# 'DeedOwner3NameFirst',
# 'DeedOwner4NameFirst',
# 'CompanyFlag',
# 'PropertyUseGroup','AreaBuilding','BathCount','BedroomsCount', \
# 'HVACCoolingDetail','HVACHeatingDetail','Fireplace','Pool']
#
# df2 = df2[cols_2]
#
# print 'Done!'
#
# df3 = pd.merge(df1,df2,how='inner',on='[ATTOM ID]')
#
#
#
# pth = '../../AIRDNA_AVM_0001/AIRDNA_AVM_0001.txt'
#
# lst = []
# with open(pth,'r') as f:
#     first_line = f.readline()
#     cols = first_line.strip().split('||')
#     for line in f:
#         line = line.strip().split('||')
#         lst.append(line)
#
# df4 = pd.DataFrame(lst,columns = cols)
#
# print 'Full load done ...'
#
# cols_1 = ['[ATTOM ID]','EstimatedValue']
#
# df = df[cols_1]

# Colorado

def _haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees). 3956 is radius of earth (mi).

    Outputs distance between two lat/long pairs in km
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def checkFirstName(firstName,fullName):
    if (firstName!=None and type(firstName)!=float):
        return firstName
    else:
        if (fullName!=None and type(fullName)!=float and (',' in fullName)):
            namesplit = fullName.split(',')[1]
            if len(namesplit)>0:
                return namesplit.split()[0]
            else:
                return ''
        else:
            return ''

def findNearbyProperties(item):
    dist = _haversine(lng,lat,item[1]['PropertyLongitude'],item[1]['PropertyLatitude'])

    if dist<=num_km:
        attom_id = item[1]['[ATTOM ID]']
        item_bed = item[1]['BedroomsCount']
        item_bath = item[1]['BathCount']
        item_name = item[1]['name']

        if abs(item_bed - beds)<=1 and abs(item_bath - baths)<=0.5:
            nearby.append((attom_id,dist,item_bed,item_bath,item_name))



df_full = pd.read_csv('../documents/tax_assessor_denver.csv',index_col=0)
df = df_full[(df_full['PropertyAddressState']=='CO') & (df_full['CompanyFlag']!='Y')]

cols = ['[ATTOM ID]','PropertyLatitude','PropertyLongitude','PropertyAddressFull','PropertyAddressCity','PropertyAddressState','PropertyAddressZIP','BedroomsCount','BathCount','PartyOwner1NameFull','PartyOwner1NameFirst']

df = df[cols]

df['firstname'] = df.apply(lambda row: checkFirstName(row['PartyOwner1NameFirst'],row['PartyOwner1NameFull']),axis=1)

df['name']=df['firstname'].apply(lambda x: ' '.join([x.replace(',',' ').replace('amp;','').replace('&','').upper().split() if (x!=None and type(x)!=float) else '' ][0]))

df['PropertyAddressZIP'] = df['PropertyAddressZIP'].apply(lambda x: [int(x) if (x!=None and type(x)!=float) else 0][0])
# df.drop('PartyOwner1NameFull',inplace=True)


query = '''

select p.id,p.airbnb_property_id,p.latitude,p.longitude,p.bedrooms,p.bathrooms,p.room_type,p.airbnb_host_id,au.first_name from property p
join airbnb_user au on au.id=p.airbnb_host_id
where p.city_id=59380
and c_days_r_ltm>0
and au.first_name is not null
and property_type in ('House','Townhouse')
order by p.id desc
'''

airbnb_df = airdna_query(query)
airbnb_df['name']=airbnb_df['first_name'].apply(lambda x: ' '.join([x.replace('amp;','').replace('&','').upper().split() if x else '' ][0]))

num_km = 0.4

df_subset = df[['[ATTOM ID]','BedroomsCount','BathCount','name','PropertyLongitude','PropertyLatitude']]

for row in airbnb_df.iterrows():

    prop_id = row[1]['airbnb_property_id']
    lat = row[1]['latitude']
    lng = row[1]['longitude']
    beds = row[1]['bedrooms']
    baths = row[1]['bathrooms']
    name = row[1]['name']
    nearby = []

    print '*-----------------------------*'
    print prop_id,name,beds,baths
    print '*-----------------------------*'

    # start = time.time()
    # cpu_processes=multiprocessing.cpu_count()
    # pool = multiprocessing.Pool(processes=cpu_processes)
    # iterable=df_subset.iterrows()
    # results = pool.map(findNearbyProperties, iterable)
    # pool.close()
    # end = time.time()
    # pdb.set_trace()

    for item in df_subset.iterrows():

        dist = _haversine(lng,lat,item[1]['PropertyLongitude'],item[1]['PropertyLatitude'])

        if dist<=num_km:
            attom_id = item[1]['[ATTOM ID]']
            item_bed = item[1]['BedroomsCount']
            item_bath = item[1]['BathCount']
            item_name = item[1]['name']

            if abs(item_bed - beds)<=1 and abs(item_bath - baths)<=0.5:
                nearby.append((attom_id,dist,item_bed,item_bath,item_name))

    df_nearby = pd.DataFrame(nearby,columns=['attom_id','dist','beds','baths','name'])

    df_nearby['ratio'] = df_nearby['name'].apply(lambda x: who.ratio(name,x))

    df_nearby.sort_values(by='ratio',axis=0,ascending=False,inplace=True)

    print df_nearby

    top_matches = df_nearby[df_nearby['ratio']==df_nearby.ratio.max()]
    top_attom_ids = top_matches['attom_id'].values

    webbrowser.open_new('https://www.airbnb.com/rooms/{}'.format(prop_id))
    for a in top_attom_ids:
        addr = ' '.join(df[df['[ATTOM ID]'] == a][['PropertyAddressFull','PropertyAddressCity','PropertyAddressState']].values[0])
        print "ATTOM ID: "+str(a)
        print "ADDRESS: "+addr
        webbrowser.open("http://www.google.com/maps/place/"+addr)

    pdb.set_trace()
    # break
    # nearby_names = [txt[4] for txt in nearby]

    # tfidf = TfidfVectorizer()
    # tfidf_matrix = tfidf.fit_transform(nearby_names)
    # tfidf_prop = tfidf.fit_transform((name,))
    # print tfidf_matrix.shape

    # print cosine_similarity(tfidf_matrix[-1:], tfidf_matrix)





# df[df['[ATTOM ID]']==]
