import sqlite3 as sql
import os

#images are stored in /static/u_images

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

def getImageById(nId):
    out = []
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id, title, description, tags, publisher, file_path, publish_time FROM images WHERE id=?",(nId,))
        for info in cur:
             out.append({
                "Id" : info[0],
                "Title": infog[1],
                "Description": info[2],
                "Tags": info[3],
                "Publisher": info[4],
                "Path": info[5],
                "Publication Time": info[6]
            })
        cur.close()

    if len(out) == 0:out.append({"Id" : None, "Title": None, "Description": None, "Tags": None, "Publisher": None, "Path": None, "Publication Time": None})
    return out

def addImage(sPath, sTitle, nOwner, sDescription, sTags):
    nTime = int(time.time())
    with sql.connect(DB_PATH) as db:
        db.execute("INSERT INTO images(title, description, tags, publisher, file_path, publish_time) VALUES (?,?,?,?,?,?)",
            (sTitle, sDescription, sTags, nOwner, sPath, nTime))
        db.commit()

def getImageByTitle(sTitle):
    out = []
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id, title, description, tags, publisher, file_path, publish_time FROM images WHERE title=?",(sTitle,))
        for info in cur:
             out.append({
                "Id" : info[0],
                "Title": info[1],
                "Description": info[2],
                "Tags": info[3],
                "Publisher": info[4],
                "Path": info[5],
                "Publication Time": info[6]
            })
            cur.close()
    if len(out) == 0:out.append({"Id" : None, "Title": None, "Description": None, "Tags": None, "Publisher": None, "Path": None, "Publication Time": None})
    return out
