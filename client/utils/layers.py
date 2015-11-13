# -*- coding: utf-8 -*-

from data import database
import os

def getLayerInformations(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, layer.user, user.name ,chapter.id, chapter.name, layer.date, layer.validated, layer.basedOn, user.id FROM layer INNER JOIN chapter ON chapter.id = layer.chapter INNER JOIN user ON user.id = layer.user WHERE layer.id = '"+ str(id) +"'")).fetchone()
	database.close(cnx)
	return res

def getLayersForUser(user):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, layer.user, lesson.name, chapter.name, layer.date,layer.validated FROM layer INNER JOIN chapter ON chapter.id = layer.chapter INNER JOIN lesson ON lesson.id = chapter.lesson WHERE layer.user = '"+ str(user) +"'")).fetchall()
	database.close(cnx)
	return res

def removeLayer(id):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("DELETE FROM layer WHERE id='"+ str(id) +"'")
	database.save(cnx)
	database.close(cnx)
	os.remove("./../data/layer/"+id+".html")

def getLayersForChapter(id):
	cnx = database.init("./../data/bdd.sq3")
	l = (cnx[1].execute("SELECT layer.id, user.name, layer.date, layer.validated, layer.basedOn, user.id FROM layer LEFT JOIN user ON user.id = layer.user WHERE layer.chapter = '"+ str(id) +"' AND layer.validated = 'True'")).fetchall()
	res = (cnx[1].execute("SELECT layer.id, user.name, layer.date, layer.validated, layer.basedOn, user.id FROM layer LEFT JOIN user ON user.id = layer.user WHERE layer.chapter = '"+ str(id) +"' AND NOT layer.validated = 'True'")).fetchall()
	for re in res:
		l.append(re)
	database.close(cnx)
	return l

def getLayerContent(id):
	try:
		data = open("./../data/layer/"+str(id)+".html", "r")
		return data.read()
	except IOError:
		return "<center><h1>Aucune donnée trouvée pour ce calque...</h1></center>"

def lastLayerId():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT id FROM layer")).fetchall()
	database.close(cnx)
	return res[len(res)-1][0]

def addLayer(basedOn, user, chapter, date, content):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO layer(basedOn, user, chapter, date, validated) VALUES ('"+ str(basedOn) +"', '"+ str(user) +"','"+ str(chapter) +"','"+ str(date) +"', 'False')")
	database.save(cnx)
	database.close(cnx)
	fil = open("./../data/layer/"+str(lastLayerId())+".html", "w")
	render = unicode(content).encode("utf-8")
	fil.write(render)
	fil.close()
	notification.addCalqueCreationNotification(user, lastLayerId())
