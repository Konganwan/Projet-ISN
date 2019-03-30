import json

LOOKUP_TABLE = []
with open("config.json") as fi:
    LOOKUP_TABLE = json.load(fi)["URLLookupTable"]

def toUrlCode(number):
    code = hex(number)[2:]
    code = "0"*(8-len(code)) + code
    return code

def toImageId(code):
    return eval("0x"+code)
    
