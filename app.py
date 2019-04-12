import cherrypy as cp


import json
import user_database as users
import image_database as images


class Webapp(object):
    """docstring for Webapp."""
    def __init__(self):
#        fi = open("config.json")
#        config = json.load(fi)
        users.tableSetup()
        images.tableSetup()

    @cp.expose(alias="home")
    def index(self):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            htmlContent = ""
            with open("pages/home/not-connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(img_mv="",img_rec="")
        else:
            htmlContent = ""
            with open("pages/home/connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[1],img_rec="", img_mv="")

    @cp.expose(alias="view")
    def show_image(self, iid=0):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            con = False
            path = "pages/view/not-connected.html"
        else:
            con = True
            path = "pages/view/connected.html"
        htmlContent = ""
        with open(path) as page:
            for line in page:
                htmlContent = htmlContent + line
        try: ipath = getImagePath(int(iid))
        except: ipath = ""
        if con:
            return htmlContent.format(name=getUserById(cp.session['logged_as'])[1], img=ipath)
        else:
            return htmlContent.format(img=ipath)

    @cp.expose
    def login(self,fail=""):
        htmlContent = ""
        with open("pages/login/login.html") as page:
          line = " "
          while not line == "":
              line = page.readline()
              htmlContent = htmlContent + line
        return htmlContent.format(fail=fail,Nom_site="Site")

    @cp.expose
    def disconect(self):
        cp.session['logged_as'] = None
        return self.index()

    @cp.expose
    def signup(self):
        return open("pages/signup/signup.html")

    @cp.expose
    def login_status(self,mail,pwd):
        if users.chekUserExists(mail) and users.checkUserPassword(pwd, mail):
            cp.session['logged_as'] = users.getUserByMail(mail)[0]
            return  self.index()
        else:
            return self.login(fail="Erreur - Adresse et/ou mot de passe incorrect")

    @cp.expose
    def signup_status(self,name,mail,pwd,cpwd):
        if cpwd == pwd and not users.chekUserExists(mail):
            users.addUser(name,pwd,mail)
            cp.session['logged_as'] = users.getUserByMail(mail)[0]
            return open("pages/signup_s/success.html")
        else:
            return open("pages/signup_s/failure.html")

    @cp.expose
    def search_results(self,query):
        return open("search_results.html")
