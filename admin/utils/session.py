# -*- coding: utf-8 -*-

from data import database
import md5

secret_cookie_key = "Je ne sais pas quoi mettre"

def checkCredentials(user, password):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT name, password FROM user WHERE name='"+user+"' AND password='"+password+"' AND admin='True'")).fetchall()
	if len(res) != 1:
		return False
	return True

def createSession(user, password, response):
	m = md5.new()
	m.update(user+password)
	c = m.digest()
	response.set_cookie("credentials", str(c), secret=secret_cookie_key)

def checkSession(request):
	if request.get_cookie("credentials", secret=secret_cookie_key) == None or request.get_cookie("credentials", secret=secret_cookie_key) == "" :
		return False
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT id, name, password FROM user WHERE admin = 'True'")).fetchall() 
	for re in res:
		m = md5.new()
		m.update(re[1]+re[2])
		c = m.digest()
		if c == request.get_cookie("credentials", secret=secret_cookie_key):
			return re[0]
	return False

def closeSession(response):
	response.set_cookie("credentials", "", secret=secret_cookie_key)