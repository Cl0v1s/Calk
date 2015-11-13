# -*- coding: utf-8 -*-

from bottle import *
from utils import users
from utils import lessons
from utils import chapters
from utils import layers
from utils import comments
from utils import session
from data import database

def isAuthenticated():
	if not session.checkSession(request):
		redirect("/login")

@route("/")
def base():
	isAuthenticated()
	redirect("/index")

#page de login
@route("/login")
def login():
	return template("login")

#page gerant la verification de l'authenticite de l'admin
@route("/auth", method="POST")
def auth():
	user = request.forms.user
	password = request.forms.password
	if session.checkCredentials(user, password):
		session.createSession(user, password, response)
		return template("achieved", {"message":"Vous etes maintenant connectes au service d'administration.", "link": "/index"})
	else:
		return template("achieved", {"message": "Impossible de vous authentifier, veuillez reessayer.", "link": "/login"})

@route("/disconnect")
def disconnect():
	session.closeSession(response)
	return template("achieved", {"message":"Vous etes maintenant deconnecte.", "link":"/login"})

#page premettant de naviguer entre l'ensemble des pages d'administration
@route("/index")
def index():
	isAuthenticated()
	return template("index")

#page affichhant l'ensemble des calques valides ou non
@route("/layers/<show>")
def layers_page(show):
	isAuthenticated()
	if show == "all":
		_layers = layers.getLayers()
	elif show == "ok":
		_layers = layers.getLayersValidated()
	elif show == "mod":
		_layers = layers.getLayersToValidate()
	else:
		_layers = layers.getLayer(show)

	return template("layers", {"layers": _layers})

#page permttant de realiser des actions sur les calques
@route("/layers/execute", method="POST")
def layers_execute_page():
	isAuthenticated()
	ide = request.forms.id

	if request.forms.delete == "yes":
		layers.removeLayer(ide, session.checkSession(request))
		return template("achieved", {"message": "Le calque a bien ete supprime.", "link":"/layers/mod"})

	if request.forms.validate == "yes":
		layers.validateLayer(ide)
		return template("achieved", {"message": "Le calque a bien ete valide.", "link":"/layers/mod"})

#Permet de moderer les commentaires
@route("/comments/<layer>")
def comments_page(layer):
	isAuthenticated()
	_comments = comments.getCommentsForLayer(layer)
	return template("comments", {"comments":_comments})

@route("/comments/execute", method="post")
def comments_execute_page():
	isAuthenticated()
	delete = request.forms.delete

	if delete=="yes":
		ide = request.forms.id
		layer = request.forms.layer
		comments.removeComment(ide, session.checkSession(request))
		return template("achieved", {"message": "Le commentaire a bien ete supprime", "link": "/comments/"+str(layer)})

	return template("achieved", {"message":"Aucune operation demandee", "link":"/index"})

#page permettant d'ajouter et de retirer  de nouveaux cours
@route("/lessons")
def lessons_page():
	isAuthenticated()
	_lessons = lessons.getLessons()
	return template("lessons", {"lessons": _lessons})

#page permettant d'executer des modifications sur les cours
@route("/lessons/execute", method="POST")
def lessons_execute_page():
	isAuthenticated()
	ide = request.forms.id
	delete = request.forms.delete
	add = request.forms.add
	if delete=="yes":
		lessons.removeLesson(ide)
		return template("achieved", {"message": "Cours supprime.","link":"/lessons"})
	if add=="yes":
		name = request.forms.name
		teatcher = request.forms.teatcher
		lessons.addLesson(name, teatcher)
		return template("achieved", {"message": "Cours ajoute.", "link": "/lessons"})
	return template("achieved", {"message": "Aucune operation realisee", "link": "/lessons"})	
	
#page permettant d'ajouter et de retirer des chapitres de cours 
@route("/chapters")
def chapters_page():
	isAuthenticated()
	_chapters = chapters.getChapters()
	_lessons = lessons.getLessons()
	return template("chapters", {"lessons": _lessons,"chapters": _chapters, "getLessonInformations": lessons.getLessonInformations})

#page permettant d'affecter les chapitres
@route("/chapters/execute", method="POST")
def chapters_execute_page():
	isAuthenticated()
	delete = request.forms.delete
	add = request.forms.add

	if delete=="yes":
		ide = request.forms.id
		chapters.removeChapter(ide)
		return template("achieved", {"message": "Chapitre supprime.", "link": "/chapters"})

	if add=="yes":
		name = request.forms.name
		lesson = request.forms.lesson.split(".")[0]
		chapters.addChapter(lesson, name)
		return template("achieved", {"message": "Le chapitre a bien ete ajoute.", "link": "/chapters"})

	return template("achieved", {"message": "Aucune action n'a ete effectuee.", "link": "/chapters"})

#page d'administyration des utilisateurs
@route("/users")
def users_page():
	isAuthenticated()
	_users = users.getAllUsers()
	return template("users",{"users":_users})

@route("/user/<name>")
def user_page(name):
	isAuthenticated()
	_users = []
	_users.append(users.getUserInformations(users.getUserIDByName(name)))
	return template("users", {"users": _users})

#page d'execution des modifications sr les utilisateurs
@route("/users/execute", method="POST")
def users_execute_page():
	isAuthenticated()
	ide = request.forms.id
	banned = request.forms.banned
	delete = request.forms.delete
	admin = request.forms.admin
	if delete=="yes":
		users.removeUser(ide)
		return template("achieved", {"message":"Utilisateur supprime.", "link":"/users"})
	if banned=="yes":
		users.banUser(ide)
	else:
		users.debanUser(ide)
	if admin=="yes":
		users.adminUser(ide)
	else:
		users.deadminUser(ide)
	return template("achieved", {"message": "Statut de l'utilisateur modifie.", "link": "/users"})	

#Sert les fichiers statics
@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='./static')

run(host="localhost", port=8080, debug=True, reloader=True);



