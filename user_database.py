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
                                          pwd_hash TEXT
                                          mail TEXT)""")
        db.commit()
        db.close()
    

def addUser(sName, sPwd, sMail):
    with sql.connect(DB_PATH) as db:
        sHashed=hasher.sha256(sPwd)
        db.execute("INSERT INTO users(name,pwd_hash,mail) VALUES (?,?,?)",(sName,sHashed,sMail))
        db.commit()
        db.close()

def removeUser(nUserID):
    with sql.connect(DB_PATH) as db:
        db.execute("REMOVE FROM users WHERE id=?",(nUserID,))
        db.commit()
        db.close()
    
def checkUserPassword(sGivenPwd):
    passco
    
def getUserInfo():
    pass

