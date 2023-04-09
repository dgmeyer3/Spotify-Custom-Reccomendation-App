from flask import Flask, render_template, request, jsonify
import sys
import spotipy as sp
import SpotifyHandler as sh
import time


user = sh.username
controller = sh.SpotifyHandler(user)


app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/play", methods=['GET', 'POST'])
def appPlay():
    print(controller.artistName())
    if str(request.form.get("Instruction")) == "play":
        print("playbutton pressed")
        controller.startPlayback()
        albumURL = str(controller.getAlbumURL())
        return jsonify({"notification": "play","albumCover": albumURL})
    else:     
        print(request.form.get("Instruction"))
        return jsonify({"notification": "pause","albumCover": albumURL})


@app.route("/pause", methods=['GET', 'POST'])
def appPause():
    
    if str(request.form.get("Instruction")) == "pause":
        print("buttonpause pressed")
        try:
            controller.pause()
            albumURL = str(controller.getAlbumURL())

            return jsonify({"notification": "Flask pause function succeeded!","albumCover": albumURL})
        except ValueError as e:
            #exception not working properly when user presses pause button on an already paused device ()"spotify:track:2CBDuc9O5PjkAAnc88gZwr")
            print("STARTS HERE" + str(e))
    else:
        print(request.form.get("Instruction"))
        return jsonify({"notification": "pause function failed in flask!","albumCover": albumURL})


@app.route('/next',methods=['GET', 'POST'])
def appNext():

    if str(request.form.get("Instruction")) == "next":
        print("skipping to next song...")
        controller.next()
        
        #sleep is here so the album art is grabbed AFTER the song skips. same with previous
        time.sleep(.5)

        songName = str(controller.currentSong())
        albumURL = str(controller.getAlbumURL())
        artistName = str(controller.artistName())

        return jsonify({"notification": "next","albumCover": albumURL})
    else:
        print(request.form.get("Instruction"))
        return jsonify({"notification": "next function failed in flask!","albumCover": albumURL,"title": songName, "artistName": artistName})

@app.route('/previous',methods=['GET', 'POST'])
def appPrevious():

    if str(request.form.get("Instruction")) == "previous":
        print("skipping to previous song...")
        controller.previous()

        time.sleep(.5)
        albumURL = str(controller.getAlbumURL())
        songName = str(controller.currentSong())
        artistName = str(controller.artistName())

        return jsonify({"notification": "previous","albumCover": albumURL})
    else:
        print(request.form.get("Instruction"))
        return jsonify({"notification": "previous function failed in flask!","albumCover": albumURL,"title": songName, "artistName": artistName})
    

@app.route("/queue", methods=['GET','POST'])
def appQueue():
    if str(request.form.get("Instruction")) == "uriArrayFlag":
        uriArray = request.form.getlist('seedArray[]')

        for uri in uriArray:
            try:
                controller.queue(uri)
                print(uri) 
            except sp.SpotifyException:
               return jsonify({"notification": "Invalid URI"})

        return jsonify({"notification": "queue sent"})
    else:
        print(request.form.get("Instruction"))
        return jsonify({"notification": "queue function failed in flask!"})
    
@app.route("/load", methods=['GET','POST'])
def appLoad():
        if str(request.form.get("Instruction")) == "load":
            try:
                albumURL = str(controller.getAlbumURL())
                songName = str(controller.currentSong())
                artistName = str(controller.artistName())
                
                print(albumURL)
                print(controller.currentSong())
                return jsonify({"notification": "load","title": songName,"albumCover": albumURL, "artist": artistName})
            except TypeError:
                return jsonify({"notification": "inactive"})
        else:
            return jsonify({"notification": "load failed"})

@app.route("/reccomend", methods=['GET','POST'])
def appReccomend():
    if str(request.form.get("Instruction")) == "propArrayFlag":
        propArray = request.form.getlist('propertyArray[]')
        print(propArray)

        currentSong=controller.nowPlaying()['uri']

        #this bring up a whole song, uris need to be extracted and added to queue. should that be done in the actual function?
        controller.ultraReccomend(currentSong,str(propArray[0]),str(propArray[1]),str(propArray[2]),str(propArray[3]),str(propArray[4]),str(propArray[5]))
        return jsonify({"notification": "something was reccomended, maybe"})
    else:
        return jsonify({"notification": "failure, somewhere"})