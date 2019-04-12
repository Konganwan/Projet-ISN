import threading

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
                    
        exit(0)
