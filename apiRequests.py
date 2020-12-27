import requests

import load

def doPost():
    # print(load.URL)
    data = {"name": "test"}
    requests.post(url=load.URL+"ckserver/start", data=data)