import sqlite3
from Dvd import DVD


class DVDManager:
    
    def __init__(self):
        self.conn=sqlite3.connect('collection.db')
        self.create_table()
        
    
    def create_table(self):
        request= ''' CREATE TABLE IF NOT EXISTS dvd(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            realisateur TEXT,
            annee INTEGER
        );'''
        self.conn.execute(request)
        self.conn.commit
        
    def ajouter_dvd(self, dvd):
        request = "INSERT INTO dvd (titre, annee, realisateur) VALUES('{0}','{1}','{2}')".format(dvd.titre, dvd.annee, dvd.realisateur)
        self.conn.execute(request)
        self.conn.commit()        
    
    def lister_dvd(self):
        cursor= self.conn.execute("SELECT * FROM dvd")
        for row in cursor:
            dvd = DVD(row[1], row[2], row[3])
            print("ID = " + str(row[0]) + " " + str(dvd))
    
    def supprimer_dvd(self, id):
        request = ("DELETE FROM dvd WHERE id='{0}'".format(id))
        self.conn.execute(request)
        self.conn.commit()
    
    def fermer_connexion(self):
        self.conn.close()     
        