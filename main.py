import cherrypy as cp

from app import Webapp

cp.quickstart(Webapp())
