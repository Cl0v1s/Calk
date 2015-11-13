# -*- coding: utf-8 -*-

from data import database

try:
	import md5
except: 
	import hashlib #python3 correction


secret_cookie_key = "Je ne sais pas quoi mettre"

def checkCredentials(user, password):
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT name, password FROM user WHERE name='"+user+"' AND password='"+password+"'")).fetchall()
	if len(res) != 1:
		return False
	return True

def createSession(user, password, response):

	try:
		m = md5.new()
	except:
		m = hashlib.md5();  #python3 correction
		
	m.update(user.encode("utf-8")+password.encode("utf-8"))
	c = m.digest()
	response.set_cookie("credentials", str(c), secret=secret_cookie_key)
	
def checkSession(request):
	if request.get_cookie("credentials", secret=secret_cookie_key) == None or request.get_cookie("credentials", secret=secret_cookie_key) == "" :
		return False
	cnx = database.init("./../data/bdd.sq3")
	res = (cnx[1].execute("SELECT id, name, password FROM user")).fetchall() 
	for re in res:
		try:
			m = md5.new()
		except:
			m = hashlib.md5();  #python3 correction
		m.update(re[1].encode("utf-8")+re[2].encode("utf-8"))
		c = m.digest()
		if str(c) == str(request.get_cookie("credentials", secret=secret_cookie_key)):
			return re[0]
	return False

def closeSession(response):
	response.set_cookie("credentials", "", secret=secret_cookie_key)