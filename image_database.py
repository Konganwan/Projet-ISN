import sqlite3 as sql
import os

#images are stored in /static/u_images

DB_PATH = 'db.db'

def toUrl(number):
    code = hex(number)[2:]
    code = "0"*(8-len(code)) + code
    return code

def toId(code):
    return eval("0x"+code)

def tableSetup():
    try:
        with sql.connect(DB_PATH) as db:
            db.execute("""CREATE TABLE images (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                              title TEXT,
                                              desc TEXT,
                                              tags TEXT,
                                              pub INTEGER,
                                              path TEXT,
                                              ptime INTEGER)""")
            db.commit()
    except:
        pass

def getImagePath(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT path FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]
    return "None"

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
        cur.execute("SELECT pub FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageDesc(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT desc FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageTime(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT ptime FROM images WHERE id=?",(nId,))
        for info in cur: return info[0]

def getImageById(nId):
    out = []
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id, title, desc, tags, pub, path, ptime FROM images WHERE id=?",(nId,))
        for info in cur:
             out.append({
                "id" : info[0],
                "title": info[1],
                "desc": info[2],
                "Tags": info[3],
                "pub": info[4],
                "path": info[5],
                "ptime": info[6]
            })
        cur.close()

    if len(out) == 0:out.append({"id" : None, "title": None, "desc": None, "Tags": None, "pub": None, "path": None, "ptime": None})
    return out

def addImage(sPath, sTitle, nOwner, sDescription, sTags, nTime):
    nId = None
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("INSERT INTO images(title, desc, tags, pub, path, ptime) VALUES (?,?,?,?,?,?)",
            (sTitle, sDescription, sTags, nOwner, sPath, nTime))
        db.commit()
        cur.execute("SELECT id FROM images WHERE path=?",(sPath,))
        for info in cur:
            nId = info[0]
        cur.close()
    return nId


def getImageByTitle(sTitle):
    out = []
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id, title, desc, tags, pub, path, ptime FROM images")
        for info in cur:
            if sTitle in info[1]:
                out.append({
                    "id" : info[0],
                    "title": info[1],
                    "desc": info[2],
                    "Tags": info[3],
                    "pub": info[4],
                    "path": info[5],
                    "ptime": info[6]
                })
        cur.close()
    if len(out) == 0:out.append({"id" : None, "title": None, "desc": None, "Tags": None, "pub": None, "path": None, "ptime": None})
    return out


