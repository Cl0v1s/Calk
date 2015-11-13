# -*- coding: utf-8 -*-

from data import database

def getChapterInformations(id):
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT chapter.id, chapter.lesson, chapter.name FROM chapter WHERE id='"+id+"'")).fetchone()
    database.close(cnx)
    return res

def getChaptersForLesson(lesson):
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT * FROM chapter WHERE lesson='"+lesson+"'")).fetchall()
    database.close(cnx)
    return res
