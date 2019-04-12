#!/usr/bin/python3.6
import cherrypy as cp
import os
from app import Webapp
from cmdinterface import CLI
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
cp.config.update({'log.screen': False,
                        'log.access_file': '',
                        'log.error_file': ''})

cli = CLI()
cli.start()
cp.quickstart(Webapp(),"/",conf)
