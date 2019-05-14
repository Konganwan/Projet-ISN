#!/usr/bin/python3.6
# -*- encoding: utf-8 -*-

# ---------------------------
# Import de librairies exterieures
# ---------------------------

import threading

# ---------------------------
# Import de fichiers locaux
# ---------------------------

import user_database as users
import image_database as images

# ---------------------------
# Tread de l'interface
# ---------------------------

class CLI(threading.Thread):
    """
    class gérant les E/S utilisateurs dans l'interface en ligne de commande
    Il s'agit d'un Thread afin de permettre une execution parallèle.
    """
    def __init__(self, engine):
        super(CLI, self).__init__()

        # Référence au serveur web afin de pouvoir l'éteindre
        self.engine = engine

# Methode principale formant la boucle de l'interface
    def run(self):
        while 1:
            # Entrée utilisateur et découpage des élements de la commande
            inp = input("App console> ")
            inp = inp.split(" ")

            # Tests
            if inp[0].lower() in ["exit","xxx","quit","q"]:
                # Sortie du programme
                break

            elif inp[0].lower() in ["users","u"]:
                # Commandes liés à la gestion des utilisateurs

                if inp[1].lower() in ["add","+"]:
                    # Ajout d'un utilisateur
                    args = inp[2:]
                    users.addUser(args[0],args[1],args[2])

                elif inp[1].lower() in ["getmail","gm"]:
                    # Récupère l'utilisateur ayant été crée avec le mail donné
                    ulist = users.getUserByMail(inp[2])
                    # Affiche sous une forme "Clé : Valeur" Les ≠ informations
                    # de l'utilisateur
                    for data in ulist:
                        print("---")
                        for field in data.keys():
                            print(f'{field} : {data[field]}')
                    print("---")

                elif inp[1].lower() in ["getid","gi"]:
                    ulist = users.getUserById(int(inp[2]))
                    for data in ulist:
                        for field in data.keys():
                            print(field,":",data[field])

                elif inp[1].lower() in ["rm","remove","-"]:
                    try:
                        arg = int(inp[2])
                        uinfo = users.removeUser(arg)
                    except Exception as e:
                        print(f'Error {e}')
                    else:
                        print(f'User n°{arg} removed')
                elif inp[1].lower() in ["gn","getname"]:

                    ulist = users.getUserByName(inp[2])
                    for data in ulist:
                        print("---")
                        for field in data.keys():
                            print(f'{field} : {data[field]}')
                    print("---")

                else:
                    print(f'Invalid subcommand: users {inp[1]}')

            elif inp[0].lower() in ["images","i"]:
                if inp[1].lower() in ["gi","getid"]:
                    ilist = images.getImageById(int(inp[2]))
                    for data in ilist:
                        print("---")
                        for field in data.keys():
                            print(f'{field} : {data[field]}')
                    print("---")

                elif inp[1].lower() in ["gt","gettitle"]:
                    ilist = images.getImageByTitle(inp[2])
                    for data in ilist:
                        print("---")
                        for field in data.keys():
                            print(f'{field} : {data[field]}')
                    print("---")

            else:
                print(f"Invalid command: {inp[0]}")

        self.engine.exit()
        exit(0)
