import sqlite3 as sql
import hashlib as hasher
import codecs
import os


DB_PATH = 'db.db'

def tableSetup():
    """Setups the constants in the database"""
    try:
        with sql.connect(DB_PATH) as db:
            db.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                              name TEXT,
                                              pwd_hash TEXT,
                                              mail TEXT)""")
            db.commit()
    except:
        pass


def addUser(sName, sPwd, sMail):
    """Adds a user in the database"""
    with sql.connect(DB_PATH) as db:
        sHashed=hasher.sha256(codecs.encode(sPwd)).hexdigest()
        db.execute("INSERT INTO users(name,pwd_hash,mail) VALUES (?,?,?)",(sName,sHashed,sMail))
        db.commit()

def removeUser(nUserID):
    with sql.connect(DB_PATH) as db:
        db.execute("REMOVE FROM users WHERE id=?",(nUserID,))
        db.commit()

def checkUserPassword(sGivenPwd, sMail):
    sGPwdHash = hasher.sha256(codecs.encode(sGivenPwd)).hexdigest()
    sStoredHash = ""
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT pwd_hash FROM users WHERE  mail=?",(sMail,))
        for info in cur:
            sStoredHash = info[0]
        cur.close()
        if sStoredHash == sGPwdHash:
            return True
        else:
            return False

def chekUserExists(sMail):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT id FROM users WHERE  mail=?",(sMail,))
        nId = None
        for info in cur:
            nId = info[0]
        cur.close()
        if nId is not None:
            return True
        else:
            return False

def getUserByMail(sMail):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE  mail=?",(sMail,))
        for info in cur:
            return info
        cur.close()

def getUserById(nId):
    with sql.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE  id=?",(nId,))
        for info in cur:
            return info
        cur.close()
