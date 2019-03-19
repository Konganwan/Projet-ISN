import cherrypy as cp

class App(object):
    
    @cp.expose
    def index(self):
            print("coucou")
        return "<h1>Test</h1><a href='/test'>Hey</a>"
    
    @cp.expose
    def test(self):
        return open("U:\\antoine.combet\\Mes documents\\ISN\\Projet\\machin.html")
        
cp.quickstart(App())