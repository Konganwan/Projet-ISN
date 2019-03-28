import sqlite3 as sql
import os


DB_PATH = None

def constantSetup(sDataBasePath):
    global DB_PATH
    DB_PATH = sDataBasePath

def tableSetup():
    with sql.connect(DB_PATH) as db:
        db.execute("""CREATE TABLE images (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                          title TEXT,
                                          description TEXT,
                                          tags TEXT,
                                          publisher INTEGER,
                                          file_path TEXT,
                                          publish_date DATE)""")
        db.commit()
        db.close()

def getImagePath(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT file_path FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageTitle(nId): pass

def getImageTags(nId): pass

def getImageOwner(nId): pass

def getImageDesc(nId): pass

def getImageDate(nId): pass

def getImageInfo(nId): pass
