import cherrypy as cp

import time
import json
import user_database as users
import image_database as images


class Webapp(object):
    """docstring for Webapp."""
    def __init__(self):
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
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0]["name"],img_rec="", img_mv="")

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
        try: ipath = images.getImagePath(int(iid))
        except: ipath = ""
        if con:
            return htmlContent.format(name=getUserById(cp.session['logged_as'])[0]["name"], main_content=ipath)
        else:
            return htmlContent.format(main_content=ipath)

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
    def signup(self,fail=""):
        htmlContent = ""
        with open("pages/signup/signup.html") as page:
          line = " "
          while not line == "":
              line = page.readline()
              htmlContent = htmlContent + line
        return htmlContent.format(fail=fail,Nom_site="Site")

    @cp.expose
    def login_status(self,mail,pwd):
        if users.checkUserExists(mail) and users.checkUserPassword(pwd, mail):
            cp.session['logged_as'] = users.getUserByMail(mail)[0]["id"]
            return  self.index()
        else:
            return self.login(fail="Erreur - Adresse et/ou mot de passe incorrect")

    @cp.expose
    def signup_status(self,name,mail,pwd,cpwd):
        if cpwd == pwd and not users.checkUserExists(mail):
            users.addUser(name,pwd,mail)
            cp.session['logged_as'] = users.getUserByMail(mail)[0]["id"]
            return self.index()
        else:
            error_message = ""
            if cpwd != pwd and users.checkUserExists(mail): error_message = "Erreur - Le mot de passe de confirmation n'est pas le même que le mot de passe choisi. Erreur - Addresse E-Mail déjà utilisée."
            elif cpwd != pwd: error_message = "Erreur - Le mot de passe de confirmation n'est pas le même que le mot de passe choisi."
            elif users.checkUserExists(mail): "Erreur - Addresse E-Mail déjà utilisée."
            return self.signup(fail=error_message)

    @cp.expose
    def search_results(self,query=""):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            htmlContent = ""
            with open("pages/search_res/not-connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(res="Work In Proress")
        else:
            htmlContent = ""
            with open("pages/search_res/connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0][1],res="Work In Proress")
    @cp.expose
    def publish(self):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            return self.login(fail="Pour pouvoir publier, vous devez être connecté")
        else:
            htmlContent = ""
            with open("pages/publish/connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0]["name"],Nom_site="Site")

    @cp.expose
    def publish_status(self, image,title,desc,tags):
        if desc == "": desc = "Aucune description fournie"
        nTime = time.time()
        sPath="static/u_images/{uid}_{t}_u.{ext}".format(uid=str(cp.session['logged_as']), t=str(nTime), ext=image.filename.split(".")[-1])
        with open(sPath,"wb") as out:
            while True:
                data = image.file.read(8192)
                if not data:
                    break
            out.write(data)
        taglist = tags.split(",")
        sTags = ""
        for i in taglist:
            if not i == "":
                sTags = sTags + "[" + i.strip() + "]"

        nId = images.addImage(sPath, title, cp.session['logged_as'], desc, sTags, nTime)
        return """nId"""
