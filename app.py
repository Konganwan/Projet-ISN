import cherrypy as cp


import json
import user_database as users
import image_database as images


class Webapp(object):
    """docstring for Webapp."""
    @cp.expose()
    def index(self):
        return open("page1.html")
