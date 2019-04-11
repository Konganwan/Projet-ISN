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

    @cp.expose(alias="home")
    def index(self):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            return open("pages/home/not-connected.html")
        else:
            htmlContent
            with open("pages/home/connected") as page:
                htmlContent = htmlContent + page.readline()
            return
            hgtmlContent.format(uName=getUserById(cp.session['logged_as'])[1])

    @cp.expose(alias="view")
    def show_image(self, iid=0):
        return open("pages/view/not-connected.html")
        htmlContent = str(page.readbytes(0xffffffffffff))
        return htmlContent.format(images.getImagePath(int(iid)))

    @cp.expose
    def login(self):
      return open("pages/login/login.html")

    @cp.expose
    def signup(self):
        return open("pages/signup/signup.html")

    @cp.expose
    def login_status(self,mail,pwd):
        if users.chekUserExists(mail) and users.checkUserPassword(pwd, mail):
            cp.session['logged_as'] = users.getUserByMail(mail)[0]
            return  open("pages/login_s/success.html")
        else: return open("pages/login_s/failure.html")

    @cp.expose
    def signup_status(self,name,mail,pwd,cpwd):
        if cpwd == pwd and not users.chekUserExists(mail):
            users.addUser(name,pwd,mail)
            cp.session['logged_as'] = getUserByMail(mail)[0]
            return open("pages/signup_s/success.html")
        else:
            return open("pages/signup_s/failure.html")

    @cp.expose
    def search_results(self,query):
        return open("search_results.html")
