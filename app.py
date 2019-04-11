import cherrypy as cp


import json
import user_database as users
import image_database as images


class Webapp(object):
    """docstring for Webapp."""
    def __init__(self):
#        fi = open("config.json")
#        config = json.load(fi)
        users.constantSetup("db.db")
        users.tableSetup()
        images.constantSetup("db.db")
        images.tableSetup()

    @cp.expose()
    def index(self):
        if 'logged_as' not in cp.session or cp.session['logged_as'] = None:
            return open("home/not-connected.html")
        else:
            htmlContent
            with open("home/connected") as page:
                htmlContent = htmlContent + page.readline()
            return
            hgtmlContent.format(uName=getUserById(cp.session['logged_as'])[1])
    @cp.expose()
    def show_image(self, iid=0):
        return open("page3.html")
        htmlContent = str(page.readbytes(0xffffffffffff))
        return htmlContent.format(images.getImagePath(int(iid)))

    @cp.expose
    def login(self):
      return open("login.html")

    @cp.expose
    def signup(self):
        return open("signup.html")

    @cp.expose
    def login_status(self,mail,pwd):
#        if users.chekUserExists(mail) and checkUserPassword(pwd, mail):
#
        return "Under Construction"

    @cp.expose
    def signup_status(self,name,mail,pwd,cpwd):
        return open("signup_status.html")

    @cp.expose
    def search_results(self,query):
        return open("search_results.html")
