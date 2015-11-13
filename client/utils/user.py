# -*- coding: utf-8 -*-

from data import database

def getUserInformations(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT user.id, user.name, user.mail, user.firstName, user.lastName, user.admin, COUNT(layer.id), COUNT(comments.id), user.picture FROM user LEFT JOIN layer ON layer.user = user.id LEFT JOIN comments ON comments.user = user.id GROUP BY user.id, user.name, user.mail, user.firstName, user.lastName, user.admin HAVING user.id = '"+ str(id) +"' ")).fetchone()
	database.close(cnx)
	return res

def updateUserInformation(id, variable, value):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE user SET "+ str(variable) +"='"+ str(value) +"' WHERE user.id = '"+ str(id) +"'")
	database.save(cnx)
	database.close(cnx)


def userFollows(user, follow):
	cnx = database.init("./../data/bdd.sq3")
	res = cnx[1].execute("SELECT * FROM follow WHERE user='"+ str(user) +"' AND follow='"+ str(follow) +"'").fetchall()
	database.close(cnx)
	if len(res) >= 1:
		return True
	return False

#"SELECT user.id, user.name, user.mail, user.firstName, user.lastName, user.admin, COUNT(layer.id), COUNT(comments.id) FROM user INNER JOIN layer ON layer.user = user.id INNER JOIN comments ON comments.user = user.id GROUP BY user.id, user.name, user.mail, user.firstName, user.lastName, user.admin HAVING user.id = '"+id+"'"

def getUserNotifications(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM notification WHERE user = '"+ str(id) +"'")).fetchall()
	database.close(cnx)
	return res

def getUserFollow(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT user.id, user.name, user.mail, user.firstName, user.lastName, user.picture FROM follow INNER JOIN user ON user.id = follow.follow WHERE user = '"+ str(id) +"'")).fetchall()
	database.close(cnx)
	return res

def getUserFollowed(id):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT user.id, user.name, user.mail, user.firstName, user.lastName, user.picture FROM follow INNER JOIN user ON user.id=follow.user WHERE follow = '"+ str(id) +"'")).fetchall()
	database.close(cnx)
	return res

def followUser(id_user, id_user_followed):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO follow (user, follow) VALUES ('"+ str(id_user) +"', '"+ str(id_user_followed) +"')")
	database.save(cnx)
	database.close(cnx)
	notification.addFollowNotification(id_user, id_user_followed)

def unfollowUser(id_user, id_user_followed):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("DELETE FROM follow WHERE user='"+str(id_user)+"' AND follow='"+str(id_user_followed)+"' ")
	database.save(cnx)
	database.close(cnx)
	notification.addUnfollowNotification(id_user, id_user_followed)

def followsUser(id_current_user, id_user):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM follow WHERE user = '"+ str(id_current_user) +"' AND follow = '"+ str(id_user) +"'")).fetchall()
	database.close(cnx)
	if len(res) > 0:
		return True
	return False
