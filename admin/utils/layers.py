# -*- coding: utf-8 -*-

from data import database
import os
import notification

def getLayersToValidate():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, user.name, chapter.name, layer.date, layer.validated FROM layer INNER JOIN chapter ON layer.chapter = chapter.id INNER JOIN user ON user.id = layer.user WHERE layer.validated = 'False'")).fetchall()
	database.close(cnx)
	return res

def getLayersValidated():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, user.name, chapter.name, layer.date, layer.validated FROM layer INNER JOIN chapter ON layer.chapter = chapter.id INNER JOIN user ON user.id = layer.user WHERE layer.validated = 'True'")).fetchall()
	database.close(cnx)
	return res

def getLayers():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, user.name, chapter.name, layer.date, layer.validated FROM layer INNER JOIN chapter ON layer.chapter = chapter.id INNER JOIN user ON user.id = layer.user")).fetchall()
	database.close(cnx)
	return res

def getLayer(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer.id, user.name, chapter.name, layer.date, layer.validated FROM layer INNER JOIN chapter ON layer.chapter = chapter.id INNER JOIN user ON user.id = layer.user WHERE layer.id = '"+ str(id) +"'")).fetchone()
	database.close(cnx)
	lis = []
	lis.append(res)
	return lis

def removeLayer(id, admin):
	notification.addLayerSuppressionNotification(id, admin)
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("DELETE FROM layer WHERE id ='"+ str(id) +"'")
	#TODO: ajouter validation
	database.save(cnx)
	database.close(cnx)
	os.remove("/data/layer/"+ str(id) +".html")
	
def validateLayer(id):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE layer SET validated='True' WHERE id = '"+ str(id) +"'")
	#TODO: ajouter notify user
	database.save(cnx)
	database.close(cnx)

def getLayerContent(id):
	try:
		data = open("./../data/layer/"+str(id)+".html", "r")
		return data.read()
	except IOError:
		return "<center><h1>Aucune donnée trouvée pour ce calque...</h1></center>"