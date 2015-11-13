# -*- coding: utf-8 -*-

from data import database
from utils import notification

def getCommentsForLayer(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT comments.id, user.id, user.name, comments.date, comments.content, user.picture FROM comments INNER JOIN user ON user.id = comments.user WHERE comments.layer='"+id+"'")).fetchall()
	database.close(cnx)
	return res

def addComment(user, layer, date, content):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO comments(layer, user, date, content) VALUES ('"+str(layer)+"','"+str(user)+"','"+str(date)+"','"+str(content)+"')")
	database.save(cnx)
	database.close(cnx)
	notification.addCommentNotification(user, layer)
