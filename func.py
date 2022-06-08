import folium
import requests


def jsontogeojson(data):
    source = {
        "type": "FeatureCollection",
        "name": "FileJson",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": []
    }
    for boucle in data:
        sourceFeature = {
            "type": "Feature",
            "properties": boucle,
            "geometry": {
                "type": "Point",
                "coordinates": [boucle['Longitude'] ,boucle['Latitude'] ]}
        }
        source["features"].append(sourceFeature)
        return source


def getInfo ():
    # -------- Create a connection with the database via an API -------------------
    response = requests.get("https://raw.githubusercontent.com/Yacine-ben1/MAPS/main/dbapi.json").json()
    #response = requests.get("dbapi.json").json()

    #---------------------------------------------
    #---------------------------------
    donnee = []
    for apidata in response:
        #-------------------Data processing  ------------------------------
        if apidata['LocalisationRelief'] != '':
            if apidata['LocalisationRelief'] != 'Unknown':
                if apidata['Longitude'] != '':
                    apidata['Longitude'] = float(apidata['Longitude'])
                    lon=apidata['Longitude']
                if apidata['Latitude'] != '':
                    apidata['Latitude'] = float(apidata['Latitude'])
                    lat =apidata['Latitude']
                    #-------------------------------------------------------------------

                    donnee.append(apidata)
    return donnee





