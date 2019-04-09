import cherrypy as cp

from app import Webapp
conf ={
    '/':{},
    '/static':{
        'tools.staticdir.on':True,
        'tools.staticdir.dir':'./static'
    }
}
cp.quickstart(Webapp())
