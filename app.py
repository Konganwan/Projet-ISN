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

        try: ipath = images.getImagePath(images.toId(iid))
        except: ipath = ""

        try: title = images.getImageTitle(images.toId(iid))
        except: title = ""

        try:
            ddesc = images.getImageDesc(images.toId(iid))
            dlist = ddesc.split("\n")
            desc = ""
            for i in dlist:
                desc = desc + "<p>" + i + "</p>"
        except:
            desc = ""

        try: own = users.getUserById(images.getImageOwner(images.toId(iid)))[0]["name"]
        except: own = ""

        if con:
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0]["name"], main_content=ipath, ititle=title, desc=desc, own=own)
        else:
            return htmlContent.format(main_content=ipath, ititle=title, desc=desc, own=own)

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
    def search_results(self,q=""):
        tags = []
        tagging=False
        current=""
        kwds=[]
        for i in q:
            if i == '[' and not tagging:
                if len(current)>0:
                    kwds.append(current)
                    current = ""
                tagging=True
            elif i == ']' and tagging:
                tags.append(current)
                current=""
                tagging = False
            else:
                current=current+i
        if len(current)>0:
            kwds.append(current)
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            htmlContent = ""
            with open("pages/search_res/not-connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(res="<p>Tags:" + str(tags) + "</p><p>Kwds:" + str(kwds) + "</p>")
        else:
            htmlContent = ""
            with open("pages/search_res/connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0][1],res="<p>Tags:" + str(tags) + "</p><p>Kwds:" + str(kwds) + "</p>")

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
    def search(self):
        if 'logged_as' not in cp.session or cp.session['logged_as'] == None:
            htmlContent = ""
            with open("pages/search/not-connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent
        else:
            htmlContent = ""
            with open("pages/search/connected.html") as page:
                for line in page:
                    htmlContent = htmlContent + line
            return htmlContent.format(name=users.getUserById(cp.session['logged_as'])[0]["name"])

    @cp.expose
    def publish_status(self, image,title,desc,tags):
        if desc == "": desc = "Aucune description fournie"
        nTime = time.time()
        sPath="static/u_images/{uid}_{t}_u.{ext}".format(uid=str(cp.session['logged_as']), t=str(nTime), ext=image.filename.split(".")[-1])
        with open(sPath,"wb") as out:
            data = image.file.read()
            out.write(data)
        taglist = tags.split(",")
        sTags = ""
        for i in taglist:
            if not i == "":
                sTags = sTags + "[" + i.strip() + "]"

        nId = images.addImage(sPath, title, cp.session['logged_as'], desc, sTags, nTime)
        return f"""{nId}"""

