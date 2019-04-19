import threading

import user_database as users
import image_database as images

class CLI(threading.Thread):
    def __init__(self, engine):
        super(CLI, self).__init__()
        self.engine = engine

    def run(self):
        while 1:
            inp = input("App console> ")
            inp = inp.split(" ")
            if inp[0].lower() in ["exit","xxx","quit","q"]:
                break
            elif inp[0].lower() in ["users","u"]:
                if inp[1].lower() in ["add","+"]:
                    args = inp[2:]
                    users.addUser(args[0],args[1],args[2])
                elif inp[1].lower() in ["getmail","gm"]:
                    ulist = users.getUserByMail("*"+inp[2]+"*")
                    for data in ulist:
                        for field in data.keys():
                            print(field,":",data[field])
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
                    ulist = users.getUserByName("*"+inp[2]+"*")
                    for data in ulist:
                        for field in data.keys():
                            print(field,":",data[field])
                else: print(f'Invalid subcommand: users {inp[1]}')

            elif inp[0].lower() in ["images","i"]:
                if inp[1].lower() in ["gi","getid"]:
                    ilist = images.getImageById(int(inp[2]))
                    for data in ilist:
                        if type(data) is dict:
                            for field in data.keys():
                                print(field,":",data[field])
                elif inp[1].lower() in ["gt","gettitle"]:
                    ilist = images.getImageByTitle("*"+inp[2]+"*")
                    for data in ilist:
                        if type(data) is dict:
                            for field in data.keys():
                                print(field,":",data[field])
            else: print(f"Invalid command: {inp[0]}")
        self.engine.exit()
        exit(0)
