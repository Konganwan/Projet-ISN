#!/usr/bin/python3.6
# -*- encoding: utf-8 -*-

# ---------------------------
# Import de librairies exterieures
# ---------------------------
import cherrypy as cp
import os

# ---------------------------
# Import de fichiers locaux
# ---------------------------

from app import Webapp
from cmdinterface import CLI

# ---------------------------
# Configuration du serveur web
# ---------------------------

conf ={
    # Paramètres généraux
    '/':{
        # Utilisation des outils de sessions utilisateurs
        'tools.sessions.on':True,

        # Tous les chemins d'accès des fichiers sont exprimés par raport au dossier du programme
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static':{
        'tools.staticdir.on':True,
        'tools.staticdir.dir':'./static'
    }
}
# Config de Logging
cp.config.update({'log.screen': False, # Disable onscreen logging to make room²
                  'log.access_file': 'access.log',
                  'log.error_file': 'error.log'})

cli = CLI(cp.engine)
cli.start()
cp.quickstart(Webapp(),"/",conf)
