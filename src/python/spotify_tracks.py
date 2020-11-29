import json
import pandas as pd 
import numpy as np 
import os
import sys
import pprint
from ytmusicapi import YTMusic

#------------------------------------------------------------------------------------
if __name__ == '__main__':

    #Init
    os.system('clear')
    pp = pprint.PrettyPrinter(indent=4)

    #Load the data
    with open('../data/deep-house-travel.json') as f:
        data = json.load(f)

    #Get the tracks class
    for item in data:
        if (item == 'tracks'):
            tracks = data[item]
        
    #Get the track class
    for item in tracks:
        if (item == 'items'):
            tracks = tracks[item]

    #Get the tracks
    result = []
    for item in tracks:
        track = item['track']
        result.append(track)
    tracks = result
    
    #Extract Name,Title
    trackinfo = []
    for i in range(len(tracks)):
        item = tracks[i]
        title = item['name']
        artists = item['artists']
        artist = (artists[0]['name'])
        trackinfo.append((artist + '|' + title))

    #Search for YouTube Vid
    ytmusic = YTMusic('headers_auth.json')
# playlistId = ytmusic.create_playlist("test", "test description")
# search_results = ytmusic.search("Oasis Wonderwall")
# ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])    

    #Save
    with open('../data/deep-house-travel.txt','w') as f:
        for item in trackinfo:
            f.write(item + '\n')