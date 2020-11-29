from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint

#----------------------------------------------------------------------------
def clientIds():

    #Set
    my_client_id = '5c7e874f0455484fa7f083ddfb00d6d3'
    my_client_secret = 'aa12f51eb9be4159b7419d628f99a9ee'
    
    #Return
    return my_client_id,my_client_secret

#----------------------------------------------------------------------------
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

#----------------------------------------------------------------------------
if __name__ == '__main__':

    #Init
    my_client_id,my_client_secret = clientIds()
    client_credentials_manager = SpotifyClientCredentials(client_id=my_client_id,client_secret=my_client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #Get Playlists
    username = 'delicieusemusique'
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print()
            print(playlist['name'])
            print ('  total tracks', playlist['tracks']['total'])
            print(dir(sp))
           # results = sp.playlist(playlist['id'],fields="tracks,next")
            #tracks = results['tracks']
            # show_tracks(tracks)
            # while tracks['next']:
            #     tracks = sp.next(tracks)
            #     show_tracks(tracks)
