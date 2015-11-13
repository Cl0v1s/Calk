import sqlite3

def init(bdd):
    connexion = sqlite3.connect(bdd);
    cursor = connexion.cursor()
    return connexion, cursor

def save(connexion):
    connexion[0].commit()
    
def close(connexion):
    connexion[0].close()