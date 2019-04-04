import cherrypy as cp


import json
import user_database as users
import image_database as images


class Webapp(object):
    """docstring for Webapp."""
    @cp.expose()
    def index(self):
        return open("page1.html")

    @cp.expose()
    def show_image(self, iid):
        page = open("show_image.html")
            page.read()

    @cp.expose
    def login(self):
      return open("login.html")

    @cp.expose
    def signup(self):
      return open("signup.html")

    @cp.expose
    def login_status(self,mail,pwd):
      return open("login_status.html")
     
