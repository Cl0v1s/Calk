# -*- coding: utf-8 -*-

from data import database
import comments
import notification

def addUser(name, password, mail):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("INSERT INTO user(name, password, mail) VALUES ('"+name+"','"+password+"','"+mail+"')")
	database.save(cnx)
	database.close(cnx)

def getUserIDByName(name):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT id FROM user WHERE name='"+name+"'")).fetchone()
	database.close(cnx)
	return res[0]

def getUserInformations(ide):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM user WHERE id='"+str(ide)+"'")).fetchone()
	database.close(cnx)
	return res

def getAllUsers():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM user")).fetchall()
	database.close(cnx)
	return res 

def getBannedUsers():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM user WHERE banned='True'")).fetchall()
	database.close(cnx)
	return res

def getNonBannedUsers():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM user WHERE NOT banned='True'")).fetchall()
	database.close(cnx)
	return res 

def banUser(id):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE user SET banned='True' WHERE id='"+id+"'")
	database.save(cnx)
	database.close(cnx)

def debanUser(id):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE user SET banned='False' WHERE id='"+id+"'")
	database.save(cnx)
	database.close(cnx)

def adminUser(id):
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE user SET admin='True' WHERE id='"+id+"'")
	database.save(cnx)
	database.close(cnx)

def deadminUser(id):
	info = getUserInformations(id)
	if info[7] == 'True' and getAdminNumber() <= 1:
		return
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("UPDATE user SET admin='False' WHERE id='"+id+"'")
	database.save(cnx)
	database.close(cnx)

def getAdminNumber():
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT * FROM user WHERE admin='True'")).fetchall()
	database.close(cnx)
	return len(res)

def removeUser(id):
	info = getUserInformations(id)
	if info[7] == 'True' and getAdminNumber() <= 1:
		return
	cnx = database.init("./../data/bdd.sq3")
	cnx[1].execute("DELETE FROM user WHERE id='"+id+"'")
	database.save(cnx)
	database.close(cnx)
	comments.removeCommentsForUser(id)
	notification.removeNotificationsForUser(id)
