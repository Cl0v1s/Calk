#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import urllib2
except:
    import urllib

from bottle import *
from utils import chapters
from utils import comments
from utils import layers
from utils import lessons
from utils import session
from utils import usefull
from utils import user


import pdfkit


def isAuthenticated():
    if not session.checkSession(request):
        redirect("/login")


@route("/")
def base():
    isAuthenticated()
    redirect("/index")

#page de login
@route("/login")
def login_page():
    return template("login")

@route("/auth", method="POST")
def auth_page():
    _user = request.forms.user
    password = request.forms.password
    if session.checkCredentials(_user, password):
        session.createSession(_user, password, response)
        return template("achieved", {"message": "Vous êtes maintenant connecté.", "link": "/index"})
    redirect("/nope")

@route("/disconnect")
def disconnect():
    session.closeSession(response)
    return template("achieved", {"message":"Vous etes maintenant deconnecte.", "link":"/login"})

@route("/nope")
def nope_page():
    return template("achieved", {"message": "Impossible de vous authentifier, veuillez reessayer.", "link":"/login"})

@route("/index")
def index_page():
    return str(session.checkSession(request))

@route("/users/execute", method="POST")
def user_execute_page():
    isAuthenticated()
    _userId = session.checkSession(request)
    _variable = request.forms.valueName
    _value = request.forms.value
    if _variable == "mail" and not "@etu.u-bordeaux.fr" in _value:
        return {"state": "Vous devez entrer votre adresse étudiant. (prenom.nom@etu.u-bordeaux.fr)"}
    if _variable == "password" and session.checkCredentials(request.forms.username, request.forms.old) == False:
        return {"state" : "Vous devez entrer votre ancien mot de passe pour pouvoir en changer."}

    if _variable == "picture":
        try:
            urllib2.urlopen(_value)
        except:
            return {"state":"Impossible de trouver l'image demandée."}

    user.updateUserInformation(_userId, _variable, _value)
    return {"state": "success"}

@route("/user/<id>")
def user_page(id):
    current_user = session.checkSession(request)
    _user = user.getUserInformations(id)
    if _user is None:
        return template("achieved", {"message": "Cet utilisateur n'existe pas", "link": "/index"})
    _followed = user.getUserFollowed(id)
    _follow = user.getUserFollow(id)
    _followedNumber = len(_followed)
    _followNumber = len(_follow)
    _layers = layers.getLayersForUser(id)

    if str(current_user) != id:
        isFollowUser = user.followsUser(current_user, id)
        return template("other", {"user" : _user, "followed" : _followed, "follow":_follow, "followedNumber": _followedNumber, "followNumber": _followNumber, "isFollowUser": isFollowUser, "layers": _layers })
    else:
        _layers = layers.getLayersForUser(id)
        _notifications = user.getUserNotifications(id)
        users = []
        try:
            for i in xrange(0,len(_notifications)):
                _user = user.getUserInformations(_notifications[i][1])
                users.append(_user[3] + " " + _user[4])
        except NameError: #Correction python 3
            for i in range(0,len(_notifications)):
                _user = user.getUserInformations(_notifications[i][1])
                users.append(_user[3] + " " + _user[4])
        _notificationsNumber = len(_notifications)
        return template("self", {"user" : _user, "followed" : _followed, "follow":_follow, "followedNumber": _followedNumber, "followNumber": _followNumber, "layers": _layers, "notifications": _notifications, "notificationsNumber": _notificationsNumber, "users": users })

@route("/user/json/<id>")
def user_json_page(id):
    use = session.checkSession(request)
    followed = 'None'
    info = user.getUserInformations(id)
    if use != False and int(use) != int(id):
        followed = user.userFollows(use, id)
    return {"firstName":info[3],"lastName": info[4], "followed":followed, "picture": info[8]}

@route("/lessons")
def lessons_page():
    _lessons = lessons.getLessons()
    return template("lessons",{"lessons":_lessons})

@route("/lesson/<id>")
def lesson_page(id):
    _chapters = chapters.getChaptersForLesson(id)
    return template("lesson", {"chapters":_chapters})

@route("/chapter/<id>", method="GET")
def chapter_page(id):
    _index = request.query.index
    if _index == None or _index == "":
        _index = 0
    else:
        _index = int(request.query.index)
    _chapter = chapters.getChapterInformations(id)
    _layers = layers.getLayersForChapter(id)
    _end = _index + 7
    if _index > len(_layers):
        _index -= 6
    _layers_content = []
    for l in _layers:
        _layers_content.append(layers.getLayerContent(l[0]))
    return template("chapter",{"layers":_layers, "layers_content": _layers_content, "chapter": _chapter, "index": _index, "end": _end})

@route("/layer/<id>")
def layer_page(id):
    _layer = layers.getLayerInformations(id)
    _layer_content = layers.getLayerContent(id)
    _comments = comments.getCommentsForLayer(id)
    _logged=False

    _user = session.checkSession(request)

    if _user != False:
        _logged=True

    return template("layer", {"layer": _layer, "layer_content": _layer_content, "comments": _comments, "logged": _logged})

@route("/layers/execute", method="POST")
def layer_execute_page():
    isAuthenticated()
    user = session.checkSession(request)
    delete = request.forms.delete
    save = request.forms.save
    if delete == "yes":
        id = request.forms.id
        userId = request.forms.user
        if str(userId) == str(user):
            layers.removeLayer(id)
            return {"state": "success"}
        else:
            return {"state": "Vous n'etes pas le proprietaire de ce calque."}
    if save == "yes":
        user = session.checkSession(request)
        basedOn = usefull.avoidJavascript(request.forms.basedOn)
        chapter = usefull.avoidJavascript(request.forms.chapter)
        content = usefull.avoidJavascript(request.forms.content)
        date = usefull.getCurrentDate()
        layers.addLayer(basedOn, user, chapter, date, content)
        return { "state": "success"}


@route("/layer/create", method="GET")
def layer_create_page():
    basedOn = request.query.basedOn
    content=""
    if basedOn != "" and basedOn != None:
        chapter = layers.getLayerInformations(basedOn)[3]
        content = open("./../data/layer/"+basedOn+".html", "r").read()
    else:
        basedOn="None"
        chapter = request.query.chapter
    return template("layer_create", {"basedOn": basedOn, "chapter": chapter, "content": content})

# génère un pdf depuis le fichier html passé en argument
@route("/layer/generate/<id>")
def layer_generate_page(id):

    source = "./../data/layer/"+id+".html"
    result = "./static/tmp/layer/"+id+".pdf"

    options = {'page-size': 'Letter','margin-top': '0.75in','margin-right': '0.75in','margin-bottom': '0.75in','margin-left': '0.75in','encoding': "UTF-8"}

    try:
        pdfkit.from_file(source, result, options=options)
        return {"state":"success", "link": result[1:]}
    except error:
        return {"state": "Une erreur est survenue, veuillez contacter l'administrateur."}

@route("/comments/execute", method="POST")
def comments_execute_page():
    isAuthenticated()
    if request.forms.send == "yes":
        _user = session.checkSession(request)
        layer = usefull.avoidJavascript(request.forms.layer)
        content = usefull.avoidJavascript(request.forms.content)
        date = usefull.getCurrentDate()
        comments.addComment(_user, layer, date, content)
        return template("achieved",{"message": "Votre commentaire a bien ete enregistré.", "link": "/layer/"+str(layer)})

@route("/follow/execute", method="POST")
def follow_execute_page():
    isAuthenticated()
    if request.forms.follow == "yes":
        _userId = session.checkSession(request)
        _user = user.getUserInformations(_userId)
        idUserFollowed = usefull.avoidJavascript(request.forms.id)
        if int(idUserFollowed) == int(_userId):
            return {"state": "same user"}
        user.followUser(_user[0], idUserFollowed)
        info = user.getUserInformations(idUserFollowed)
        return {"state":"success", "follow":info[1]}
    elif request.forms.unfollow == "yes":
        _userId = session.checkSession(request)
        _user = user.getUserInformations(_userId)
        idUserFollowed = usefull.avoidJavascript(request.forms.id)
        if int(idUserFollowed) == int(_userId):
            return {"state": "same user"}
        user.unfollowUser(_user[0], idUserFollowed)
        info = user.getUserInformations(idUserFollowed)
        return {"state":"success", "unfollow": info[1]}

#Sert les fichiers statics
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

run(host="localhost", port=8080, debug=True, reloader=True)