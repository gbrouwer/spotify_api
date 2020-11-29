import spotipy
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

#----------------------------------------------------------------------------
def clientIds():

    #Set
    my_client_id = '5c7e874f0455484fa7f083ddfb00d6d3'
    my_client_secret = 'aa12f51eb9be4159b7419d628f99a9ee'
    
    #Return
    return my_client_id,my_client_secret

#----------------------------------------------------------------------------
if __name__ == '__main__':

    #Username
    username = 'gbrouwer5151'

    #Settings
    cmd1 = "export SPOTIPY_CLIENT_ID='5c7e874f0455484fa7f083ddfb00d6d3'"
    cmd2 = "export SPOTIPY_CLIENT_SECRET='aa12f51eb9be4159b7419d628f99a9ee'"
    cmd3 = "export SPOTIPY_REDIRECT_URI='http://www.gijsjoostbrouwer.com'"
    cmd4 = "export YOUTUBE_DEV_KEY='AIzaSyDygNhHkHUQLWSNz-AFDFe33eU4n2FdFyU'"
    
    #Init
    my_client_id,my_client_secret = clientIds()
    client_credentials_manager = SpotifyClientCredentials(client_id=my_client_id,client_secret=my_client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # #Get Playlists
    # idlist = []
    # playlists = sp.user_playlists(username)
    # for playlist in playlists['items']:
    #     if playlist['owner']['id'] == username:
    #         idlist.append(playlist['id'])
    #         print(playlist['id'],playlist['name'])

    # #Download Command
    # # playlist_id = '3OcLmMGOaKBhDAPji7mTf3'
    # playlist_id = '624HWemwkr07H8B6GyLC9y'
    playlist_id = '0NLAC7syToc2g6ImWybVB4'
    cmd5 = 'spotify_dl -d -u ' + username + ' -p ' + playlist_id + ' -o . '

    #Print    
    print(cmd1)
    print(cmd2)
    print(cmd3)
    print(cmd4)
    print(cmd5)
    # # # os.system(cmd1)
    # # # os.system(cmd2)
    # # # os.system(cmd3)
    # # # os.system(cmd4)
    # # os.system(cmd5)