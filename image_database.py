import sqlite3 as sql
import os


DB_PATH = None

def constantSetup(sDataBasePath):
    global DB_PATH
    DB_PATH = sDataBasePath

def tableSetup():
    with sql.connect(DB_PATH) as db:
        db.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                          title TEXT,
                                          description TEXT,
                                          publisher INTEGER,
                                          file_path TEXT,
                                          publish_date DATE)""")
        db.commit()
        db.close()
