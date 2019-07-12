from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]


def getVersion():
    return "0.0.1"


def getShows():
    shows = []
    for showid in AVAILABE_SHOWS:
        shows.append(json.loads(getJsonFromFile(showid)))
    return shows


def getSpecificShow(show):
    specific_show = json.loads(getJsonFromFile(show))
    return specific_show


def getSpecificEpisode(showid, episodeid):
    specific_show = json.loads(getJsonFromFile(showid))
    list_episodes = specific_show["_embedded"]["episodes"]
    episode = int(float(episodeid))
    for item in list_episodes:
        if item["id"] == episode:
            return item


def get_search(my_query):
    search_result = []
    for showid in AVAILABE_SHOWS:
        specific_show = json.loads(getJsonFromFile(showid))
        list_episodes = specific_show["_embedded"]["episodes"]
        for item in list_episodes:
            if item["summary"] is not None and my_query in str(item["summary"]):
                result = {
                    'text': "%s : %s" % (specific_show["name"], item["name"]),
                    'showid': specific_show['id'],
                    'episodeid': item['id'],
                }
                search_result.append(result)

    return search_result




def getJsonFromFile(showid):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showid))
    except:
        return "{}"
