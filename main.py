#!/usr/bin/python3.6
import cherrypy as cp
import os
from app import Webapp
conf ={
    '/':{
        'tools.sessions.on':True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static':{
        'tools.staticdir.on':True,
        'tools.staticdir.dir':'./static'
    }
}
cp.quickstart(Webapp(),"/",conf)
