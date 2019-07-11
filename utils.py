from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

def getVersion():
    return "0.0.1"

def getShows():
    shows = []
    for show in AVAILABE_SHOWS:
        shows.append(json.loads(getJsonFromFile(show)))
    return shows

def getSpecificShow(show):
    specificShow = json.loads(getJsonFromFile(show))
    return specificShow

def getSpecificEpisode(episode):
    episode = json.loads(getJsonFromFile(episode))
    specififepisode = episode._embedded.episodes.id
    return specififepisode

def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"
