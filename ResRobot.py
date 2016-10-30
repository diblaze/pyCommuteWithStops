#! /usr/bin/env python3

import requests
import json

def GetStopsBasedOnName(APIKey, station_to_search_for):
    #format the request url
    request_url = "https://api.resrobot.se/v2/location.name?format=json&key={}&input={}".format(APIKey, station_to_search_for)
    #get the data
    stations = requests.get(request_url)
    #return all stations in JSON
    stations = json.loads(stations.text)

    stations_dict = {}
    for stop in stations["StopLocation"]:
        if stop["name"] not in stations_dict:
            stations_dict[stop["name"]] = stop

    return stations_dict

def GetTripBetweenStops(APIKey, stop1, stop2, date="", time="", searchForArrival=True):
    if len(time) == 0:
        return None

    #format the request url
    if len(date) == 0:
        request_url = "https://api.resrobot.se/v2/trip?key={}&originId={}&destId={}&time={}&searchForArrival=1&format=json".format(APIKey, stop1, stop2, time)
    else:
        request_url = "https://api.resrobot.se/v2/trip?key={}&originId={}&destId={}&date={}&time={}&searchForArrival=1&format=json".format(APIKey, stop1, stop2, date, time)

    #get the data
    trips = requests.get(request_url)
    #return all trips
    trips = json.loads(trips.text)

    dict_trips = {}
    for trip in trips["Trip"]:
        for leglist in trip["LegList"]:
            for leg in leglist.items():
                print(leg)             
    
    print(dict_trips)
    
    #return dict_trips

