#! /usr/bin/env python3
import ResRobot

import APIKeys
import sys
import requests, json


from datetime import datetime

def GetStopsBasedOnName(station_name):
    stops = ResRobot.GetStopsBasedOnName(APIKeys.GetAPIKey(), station_name)
    
    return stops

def SelectAStop(dict_stops):
    dict_stop_ids = {}
    choosen = False

    done = False
    while not done:
        i = 1
        for stop in dict_stops:
            dict_stop_ids[i] = dict_stops[stop]
            i += 1
        done=True


    while not choosen:
        for i in dict_stop_ids:
            print(str(i) + ": " + dict_stop_ids[i]["name"])
        
        userInput = input("Select the station you are looking for (id): ")
        userInput = int(userInput)

        if userInput in dict_stop_ids.keys():
            return dict_stop_ids[userInput]["id"]
    
    return None
            


if __name__ == "__main__":
    #get all stops
    stops = GetStopsBasedOnName("Charlottenborg C, Motala")

    #get the internal ID used by ResRobot for the station.
    stop = SelectAStop(stops)

    stops = GetStopsBasedOnName("Stora Torget, Motala")
    stop2 = SelectAStop(stops)

    ResRobot.GetTripBetweenStops(APIKeys.GetAPIKey(), stop, stop2, time="06:00")


    






