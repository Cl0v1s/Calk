# -*- coding: utf-8 -*-

from data import database

def getCommentsForLayer(ide):
    cnx = database.init("./../data/bdd.sq3")
    res = (cnx[1].execute("SELECT comments.id, comments.layer, user, comments.date, comments.content FROM comments ")).fetchall()
    #WHERE layer='"+str(ide)+"' INNER JOIN user ON user.id=comments.user INNER JOIN layer ON layer.id=comments.layer INNER JOIN chapter ON layer.chapter=chapter.id
    database.close(cnx)
    return res

def removeComment(ide):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("DELETE FROM comments WHERE id='"+str(ide)+"'")
    database.save(cnx)
    database.close(cnx)
    
def addComment(layer, user, date, content):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("INSERT INTO comments(layer, user, date, content) VALUES ('"+layer+"', '"+user+"', '"+date+"', '"+content+"')")
    database.save(cnx)
    database.close(cnx)
    
def removeCommentsForUser(ide):
    cnx = database.init("./../data/bdd.sq3")
    cnx[1].execute("DELETE FROM comments WHERE user='"+ide+"'")
    database.save(cnx)
    database.close(cnx)
    
    