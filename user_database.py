import sqlite3 as sql
import hashlib as hasher
import os


DB_PATH = os.path.dirname(__file__).join("db.db")

def constantSetup(sDataBasePath):
    global DB_PATH
    here.DB_PATH = sDataBasePath
    pass

def initTable():
    with sql.connect(DB_PATH) as db:
        db.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                          name TEXT,
                                          pwd_hash TEXT,
                                          mail TEXT)""")
        db.commit()
        db.close()
    

def addUser(sName, sPwd, sMail):
    with sql.connect(DB_PATH) as db:
        sHashed=hasher.sha256(sPwd).hexdigest()
        db.execute("INSERT INTO users(name,pwd_hash,mail) VALUES (?,?,?)",(sName,sHashed,sMail))
        db.commit()
        db.close()

def removeUser(nUserID):
    with sql.connect(DB_PATH) as db:
        db.execute("REMOVE FROM users WHERE id=?",(nUserID,))
        db.commit()
        db.close()
    
def checkUserPassword(sGivenPwd, sMail):
    sGPwdHash = hasher.sha256(sGivenPwd).hexdigest()
    sStoredHash = ""
    with sql.connect(DB_PATH).cursor() as cur:
        cur.execute("SELECT pwd_hash FROM users WHERE  mail=?",(sMail,))
        for info in cur:
            sStoredHash = info[0]
        if sStoredHash == sGPwdHash:
            return True
        else:
            return False

def chekUserExists(sMail):
    with sql.connect(DB_PATH).cursor() as cur:
        cur.execute("SELECT id FROM users WHERE  mail=?",(sMail,))
        nId = None
        for info in cur:
            nId = info[0]
        if nId is not None:
            return True
        else:
            return False
    
def getUserInfo(sMail):
    with sql.connect(DB_PATH).cursor() as cur:
        cur.execute("SELECT * FROM users WHERE  mail=?",(sMail,))
        for info in cur:
            return info


