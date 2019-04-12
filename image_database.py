import sqlite3 as sql
import os


DB_PATH = 'db.db'


def tableSetup():
    try:
        with sql.connect(DB_PATH) as db:
            db.execute("""CREATE TABLE images (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                              title TEXT,
                                              description TEXT,
                                              tags TEXT,
                                              publisher INTEGER,
                                              file_path TEXT,
                                              publish_time INT)""")
            db.commit()
    except:
        pass

def getImagePath(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT file_path FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageTitle(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT title FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageTags(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT tags FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageOwner(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT publisher FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageDesc(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT description FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageTime(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT publish_time FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageInfo(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id, title, description, tags, publisher, file_path, publish_time FROM images WHERE id=?",(nId,))
        for info in cur:
            return {
                "id" : info[0],
                "title": info[1],
                "description": info[2],
                "tags": info[3],
                "publisher": info[4],
                "file_path": info[5],
                "publish_time": info[6]
            }

def addImage(sPath, sTitle, nOwner, sDescription, sTags):
    nTime = int(time.time())
    with sql.connect(DB_PATH) as db:
        db.execute("INSERT INTO images(title, description, tags, publisher, file_path, publish_time) VALUES (?,?,?,?,?,?)",
            (sTitle, sDescription, sTags, nOwner, sPath, nTime))
        db.commit()
        db.close()
