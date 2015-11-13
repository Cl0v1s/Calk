# -*- coding: utf-8 -*-

from data import database
from utils import user
from utils import layers

# Les types de notifiactions sont :
# 0 pour les commentaires (pour le propriétaire du calque)
# 1 pour les follow
# 2 pour les unfollow
# 3 pour les ajouts de calques (pour les followers)

def addCommentNotification(_user, _layer):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO notification (user, notificator, type, layer) VALUES ('"+ str(layers.getLayerInformations(_layer)[1]) +"', '"+ str(_user) +"', '0', '"+ str(_layer) +"')")
	database.save(cnx)
	database.close(cnx)

def addFollowNotification(user, userFollowed):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO notification (user, notificator, type) VALUES ('"+ str(userFollowed) +"', '"+ str(user) +"', '1')")
	database.save(cnx)
	database.close(cnx)

def addUnfollowNotification(user, userFollowed):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO notification (user, notificator, type) VALUES ('"+ str(userFollowed) +"', '"+ str(user) +"', '2')")
	database.save(cnx)
	database.close(cnx)

def addCalqueCreationNotification(_user, layer):
	followers = user.getUserFollowed(_user)
	cnx = database.init("./../data/bdd.sq3")
	for follower in followers:
		cnx[1].execute("INSERT INTO notification (user, notificator, type, layer) VALUES ('"+ str(follower[0]) +"', '"+ str(_user) +"', '3', '"+ str(layer) +"')")
	database.save(cnx)
	database.close(cnx)
