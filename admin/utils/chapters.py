# -*- coding: utf-8 -*-

from data import database

def addChapter(lesson, name):
    if lesson == "" or name == "" or lesson == None or name == None:
        return
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("INSERT INTO chapter(lesson, name) VALUES ('"+lesson+"','"+name+"')")
    database.save(cnx)
    database.close(cnx)
    
def getChapters():
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM chapter")).fetchall()
    database.close(cnx)
    return res

def removeChapter(ide):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("DELETE FROM chapter WHERE id='"+ide+"'")
    database.save(cnx)
    database.close(cnx)