import folium
import pandas as pd
import re

def parse_data():
    df = pd.read_csv('./data/Cholera.csv')
    df['geometry'] = df['geometry'].apply(lambda x: re.sub('<.*?>', '', x))
    df['latitude'] = df['geometry'].apply(lambda x: float(x.split(',')[0]))
    df['longitude'] = df['geometry'].apply(lambda x: float(x.split(',')[1]))
    df = df.drop('geometry', axis=1)
    df_pumps = df[df['count'] == -999].reset_index(drop=True)
    return df, df_pumps

def dist(coord1, coord2):
'''
INPUT: two latitude, longitude tuples.
OUTPUT: approximate distance between.
'''
    pass

def nearest_pump(df, pump_df):
'''
For each data point, calculate distance to each pump.  Find minimum
distance, return index of pump.  Note: create a nearest_pump column
using this function.
'''
    pass

def build_map(df):
    cholera_map = folium.Map(location = [51.513, -0.137], zoom_start=17, tiles='Stamen Toner')
    for row in range(0, len(df)):
        lat = df['latitude'][row]
        lon = df['longitude'][row]
        count = df['count'][row]
        if count > 0:
            folium.CircleMarker(location = [lon, lat], color='rgba(40,52,171, 0.5)', fill_color='rgba(40,52,160, 0.5)', radius=3*count).add_to(cholera_map)
        else:
            folium.CircleMarker(location = [lon, lat], color='rgba(171,52,40, 0.8)', fill_color='rgba(171,52,40, 0.8)', radius=10).add_to(cholera_map)
    cholera_map.save('Cholera.html')

if __name__ == '__main__':
    df, df_pumps = parse_data()
    build_map(df)
