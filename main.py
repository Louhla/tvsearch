import os
from bottle import (get, post, redirect, request, route, run, static_file, error,
                    template)
import utils


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    sectionData = utils.getShows()
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/ajax/show/<filename>')
def show(filename):
    section_data = utils.getSpecificShow(filename)
    return template("./templates/show.tpl", result=section_data)


@route('/ajax/show/<showid>/episode/<episodeid>')
def showepisode(showid, episodeid):
    section_data2 = utils.getSpecificEpisode(showid, episodeid)
    return template("./templates/episode.tpl", result=section_data2)


@route('/search')
def index():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search', method="POST")
def search():
    my_query = request.POST.get("q")
    sectionTemplate = "./templates/search_result.tpl"
    sectionData = utils.get_search(my_query)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=sectionData, query=my_query)

@error(404)
def error(error):
    error_template = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=error_template, sectionData={})

if __name__ == "__main__":
    run(host='localhost', port=os.environ.get('PORT', 5000))
