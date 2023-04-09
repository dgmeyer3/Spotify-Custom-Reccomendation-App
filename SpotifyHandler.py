import sys
import spotipy
import spotipy.util as util
import random


#please manually update 
cid = ""
secret = ""
username = ""
redirect = ""

scope = 'user-read-playback-state user-modify-playback-state app-remote-control'
scope += ' user-read-recently-played user-top-read user-library-read'

class SpotifyHandler(object):
    
    #create controller object, authorize, generate token, create spotify object with token
    def __init__(self, username):        
        token = util.prompt_for_user_token(username,scope,client_id=cid,client_secret=secret, redirect_uri=redirect)
        self.sp = spotipy.Spotify(auth=token)

        self.blacklist = []

    def nowPlaying(self):
        return self.sp.current_playback()["item"]
    
    def play(self, uri=None, uris=None, context_uri=None):
        if context_uri is not None:
            self.sp.start_playback(context_uri=context_uri)
        elif uris is not None:
            self.sp.start_playback(uris=uri_list)
        elif uri is not None:
            self.sp.start_playback(uris=[uri])

    def pause(self):
        self.sp.pause_playback()

    def queue(self, uri):
        self.sp.add_to_queue(uri=uri)
        
    def next(self):
        #gets info about the song after skip in order to change album art
        self.sp.next_track()

    def previous(self):
        self.sp.previous_track()

    def track(self, uri):
        return self.sp.track(uri)

    def recommend(self, uri):
        return self.sp.recommendations(seed_tracks=[uri], limit=20)['tracks']
    
    def ultraReccomend(self, uri, BPM:None, dance:None, energy: None, live: None,inst: None, extra: None):
        
        reccomendedSong =  self.sp.recommendations(seed_tracks=[uri], target_tempo=BPM, target_danceability=dance, target_energy=energy,
                                       target_liveliness= live, target_instrumentalness=inst, target_acousticness= extra, limit=3)['tracks'][0]['uri']
        
        self.sp.add_to_queue(uri=reccomendedSong)
        
        return reccomendedSong

    def bpm(self, track_uri):
         return self.sp.audio_features(track_uri)[0]["tempo"]

    def recentlyPlayed(self):
        return self.sp.current_user_recently_played()

    def topTracks(self):
        return self.sp.current_user_top_tracks()

    def topArtists(self):
        return self.sp.current_user_top_artists()
    
    def songTime(self,track_uri):
        timeMs = float(self.sp.audio_features(track_uri)[0]["duration_ms"])
        return timeMs/1000
    
    def startPlayback(self):
        if self.sp.current_playback() != None:
            self.sp.start_playback()
            return
    def elapsedTime(self):
        timeMs = self.sp.current_playback()['progress_ms']
        return timeMs/1000
    
    def isPlaying(self):
        return self.sp.current_playback()['is_playing']
    
    def getAlbumURL(self):
        currentAlbumCover = self.sp.current_playback()["item"]["album"]["images"][1]["url"]
        return currentAlbumCover
    
    def currentSong(self):
        Song = self.sp.current_playback()["item"]["name"]
        return Song
    
    def artistName(self):
        artist = self.sp.current_playback()["item"]["album"]["artists"][0]["name"]
        return artist
            
    def closeController(self):
        pass
