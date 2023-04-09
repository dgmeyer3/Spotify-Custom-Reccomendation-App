# Spotify-Custom-Reccomendation-Tool (SCRT)

This project is a playback tool for Spotify that allows users to directly reccomend songs based off of properties defined in the SpotiPy library. By adjusting the sliders on the bottom section of the webpage, a song with similar properties will be queued!. Users can also take advantage of the playback controls & song queue list directly in the app. 

**Link to project:** (include github link when it loads)



## How It's Made:

**Tech used:** HTML, CSS, JavaScript, Jquery, Python, Flask, SpotiPy library

SpotipyHandler.py is an API that creates an object that allows the frontend to easily call the SpotiPy library. This gives SCRT access to the users Spotify account, so it is able to control playback + reccoemend songs. **users must enter their own Oauth2 client_id, client_secret, username, and redirect. Client_id & client_secret tokens can be created by following the steps here: https://spotipy.readthedocs.io/en/2.11.1/ **

The project utilized a flask server to call the python API. additionally, Jquery & Ajax are used to send information from the webpage itsself to flask, without refreshing the page.

For the Frontend, I took inspiration from the layout on https://chess.com! while the page ended up looking very different, the core layout of a flexbox within a grid allowed me to create a very standardized box layout. The page also flexes well, and works down to a minium width of a vertically standing monitor. CSS has been modified such that the display looks good across the main three browsers (Chrome, Firefox and Safari), with a standardized color/font pallate.

## Optimizations

-Sliders appeared much differently on chrome as they did on Firefox, my native browser. This was fixed by using webkit to edit the slier appearance for chrome. While the sliders still look different across browsers, all appearances now fit within the style of the app. 

-**div that appears when you hover over album cover, displaying the songs properties** : This will be pushed to the main build soon, but I wanted to provide users (and myself) with easier access to the songs properties (liveness, BPM, energy, etc). Instead of checking the terminal & reading through all of the songs information, the relevant traits are now displayed by hovering over the album.

-**toggleable play/pause button** : also will be pushed in the next update. Quality of life feature that also fixed a bug where SCRT would attempt to pause a song that was already paused, throwing an error.

## Lessons Learned:

No matter what your experience level, being an engineer means continuously learning. Every time you build something you always have those *whoa this is awesome* or *fuck yeah I did it!* moments. This is where you should share those moments! Recruiters and interviewers love to see that you're self-aware and passionate about growing.

-The biggest difficulty I had with this project was using Jquery and Ajax to send information from the webpage to flas. While I was familiar with how to send data to flask, doing so without the page refreshing was an interesting challenge to overcome. $.ajax() is a very powerful tool and it was a great experience learning how to properly send a json back and forth between a server. 

-This project began was a few hours of learning how to use Oauth2 with Spotify, and providing my application with Spotify access correctly. In addition to exporting my own credentials, SpotiPy has a number of different access levels, each allowing the API to call certain functions. 

-sp.audio_features gave a broad spectrum of information that was difficult to decode at first. Everything I could want to know about a song on spotify is stored there, but parsing it was not easy. It was always a relief to see that the correct information had displayed on the webpage, and not an abomination of json & special characters!


## Examples:


Upon the document loading, you may recieve this error:

![image](https://user-images.githubusercontent.com/90935162/230799665-13cf1cd1-ea0c-407f-b955-63ac3903aa2f.png)

Currently, SCRT can not activate a spotify session. To activate a session, please launch Spotify on a device that the user is logged in to, and the application should load successfully. As mentioned above, client tokens + username + redirect must be manually added to SpotipyHandler.py for the application to work.

Play, Pause, Next, Previous buttons: These are simple playback controls that act the same as they would in the spotify app. They also update album cover/song name/artist name within SCRT. 

The queue list takes a unique spotify track uri and adds it to the list below.
![image](https://user-images.githubusercontent.com/90935162/230799532-15424147-14f5-4dc8-9b7e-9949716e4270.png)

The uri must be in the correct format (ex: spotify:track:7lEptt4wbM0yJTvSG5EBof), or the webpage will throw an error:

![image](https://user-images.githubusercontent.com/90935162/230799635-90b15e03-1d95-4b84-8715-e6c70a6f758a.png)

To queue the added songs, press "Seed URI". 

The sliders on the bottom of the controller can are used for the reccomend function. move the sliders to your preferred setting, and press submit to queue a song with those desired properties. Please note, this function will reccomend a song similar to the one currently playing. 

