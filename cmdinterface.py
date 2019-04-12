import threading

import user_database as users

class CLI(threading.Thread):
    """Console interface for live db edit"""
    def __init__(self):
        pass

    def run():
        while 1:
            inp = input("App console> ")
            if inp.lower() in ["exit","xxx","quit","q"]:
                break
            elif inp.lower() in ["users"]:
                sc = input("Users> ")
                if sc.lower() == "add":
                    args = []
                    for arg in ("nom", "pwd", "mail"):
                        args.append(input(f'{arg}> '))
                    users.addUser(args[0],args[1],args[2])
                elif sc.lower() == "getmail":
                    arg = input("User Mail> ")
                    uinfo = users.getUserByMail(arg)
                    print(f'Id: {uinfo[0]}\nNom: {uinfo[1]}\nPwd_hash: {uinfo[2]}\nMail: {uinfo[3]}')
                elif sc.lower() == "getid":
                    arg = int(input("User ID> "))
                    uinfo = users.getUserById(arg)
                    print(f'Id: {uinfo[0]}\nNom: {uinfo[1]}\nPwd_hash: {uinfo[2]}\nMail: {uinfo[3]}')"
                elif sc.lower() in ["rm","remove"]:
                    arg = int(input("User ID> "))
                    uinfo = users.removeUser(arg)
                    print(f'User n°{arg} removed')
                else: print(f'Invalid subcommand: {sc}')
            else: print(f'Invalid command: {inp}')


        exit(0)
