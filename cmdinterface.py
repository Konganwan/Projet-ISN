import threading

import user_database as users

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
            elif inp[0].lower() in ["users"]:
                if len(inp) < 2:
                    print('Command users needs subcommand')
                    continue
                if inp[1].lower == "add":
                    args = inp[2:]
                    users.addUser(args[0],args[1],args[2])
                elif inp[1].lower() == "getmail":
                    arg = inp[2]
                    uinfo = users.getUserByMail(arg)
                    print(f'Id: {uinfo[0]}\nNom: {uinfo[1]}\nPwd_hash: {uinfo[2]}\nMail: {uinfo[3]}')
                elif inp[1].lower() == "getid":
                    arg = int(inp[2])
                    uinfo = users.getUserById(arg)
                    print(f'Id: {uinfo[0]}\nNom: {uinfo[1]}\nPwd_hash: {uinfo[2]}\nMail: {uinfo[3]}')
                elif inp[1].lower() in ["rm","remove"]:
                    try:
                        arg = int(inp[2])
                        uinfo = users.removeUser(arg)
                    except Exception as e:
                        print(f'Error {e}')
                    else:
                        print(f'User n°{arg} removed')
                else: print(f'Invalid subcommand: users {inp[1]}')
            else: print(f'Invalid command list: {inp[0]}')
        self.engine.exit()
        exit(0)
