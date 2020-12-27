import json

def load():

    data = None

    with open("secret.json") as file:
        data = json.load(file)

    global TOKEN
    global MACADDR
    global ADMINS
    global GAMES
    global URL

    TOKEN = data["token"]
    MACADDR = data["macaddress"]
    ADMINS = data["admins"]
    GAMES = data["games"]
    URL = data["url"]

    # print(TOKEN)