# -*- coding: utf-8 -*-

from data import database

def addLesson(name, teatcher):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("INSERT INTO lesson(name, teatcher) VALUES ('"+name+"','"+teatcher+"')")
    database.save(cnx)
    database.close(cnx)
    
def getLessons():
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM lesson")).fetchall()
    database.close(cnx)
    return res

def getLessonInformations(ide):
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM lesson WHERE id='"+str(ide)+"'")).fetchone()
    database.close(cnx)
    return res

def removeLesson(ide):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("DELETE FROM lesson WHERE id='"+ide+"'")
    database.save(cnx)
    cnx[1].execute("DELETE FROM chapter WHERE lesson='"+ide+"'")
    database.save(cnx)
    database.close(cnx)
