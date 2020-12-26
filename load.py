import json

def load():

    data = None

    with open("secret.json") as file:
        data = json.load(file)

    global TOKEN
    global MACADDR
    global ADMINS
    global GAMES

    TOKEN = data["token"]
    MACADDR = data["macaddress"]
    ADMINS = data["admins"]
    GAMES = data["games"]

    # print(TOKEN)