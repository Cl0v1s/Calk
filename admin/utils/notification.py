# -*- coding: utf-8 -*-

from data import database
import user
import layers

# Les types de notifiactions sont :
# 0 pour les commentaires (pour le propriétaire du calque)
# 1 pour les follow
# 2 pour les unfollow
# 3 pour les ajouts de calques (pour les followers)
# 4 pour les suppressions de commentaires
# 5 pour les suppressions de calques
# 6 pour la validation de calques

def addCommentSuppressionNotification(id, admin):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT layer, user FROM comments WHERE id = '"+ str(id) +"'")).fetchone()
	cnx[1].execute("INSERT INTO notification (user, notificator, type, layer) VALUES ('"+ str(res[1]) +"', '"+ str(admin) +"', '4', '"+ str(res[0]) +"')")
	database.save(cnx)
	database.close(cnx)

def addLayerSuppressionNotification(id, admin):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT user FROM layer WHERE id = '"+ str(id) +"'")).fetchone()
	cnx[1].execute("INSERT INTO notification (user, notificator, type, layer) VALUES ('"+ str(res[0]) +"', '"+ str(admin) +"', '5', '"+ str(id) +"')")
	database.save(cnx)
	database.close(cnx)

def addLayerValidationNotification(id, admin):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT user FROM layer WHERE id = '"+ str(id) +"'")).fetchone()
	cnx[1].execute("INSERT INTO notification (user, notificator, type, layer) VALUES ('"+ str(res[0]) +"', '"+ str(admin) +"', '6', '"+ str(id) +"')")
	database.save(cnx)
	database.close(cnx)

def removeNotificationsForUser(ide):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("DELETE FROM notification WHERE user='"+ide+"'")
	database.save(cnx)
	database.close(cnx)