import cherrypy as cp
import os
from app import Webapp
conf ={
    '/':{
        #'tools.session.on':True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static':{
        'tools.staticdir.on':True,
        'tools.staticdir.dir':'./static'
    }
}
cp.quickstart(Webapp(),"/",conf)
