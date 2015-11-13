# -*- coding: utf-8 -*-

from data import database

def getLessonInformations(id):
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM lesson WHERE id='"+id+"'")).fetchone()
    database.close(cnx)
    return res

def getLessons():
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM lesson")).fetchall()
    database.close(cnx)
    return res



