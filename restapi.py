# restapi.py
import requests
import json
from jsonmerge import merge
import time
 

class ApiHandler():
    
    def __init__(self, dataEndPoint, dataHeader, ipEndPoint="http://ip-api.com/json/", ipHeader={'content-type': 'application/json'}):
        '''This initialize the class with the API  from where we want to pull the data.
           This API passed as env variable.
        '''
        self.dataEndpoint =  dataEndPoint
        self.dataHeader = dataHeader
        self.ipEndpoint =  ipEndPoint
        self.ipHeader = ipHeader
        
    
    def getDataFromApi(self, api, header, **kwargs):
        '''This API gets the data, if paginations are there it takes care. Return the data as it is.
        User of this API can convert the data into any format they want.
        '''
        print("API", api)
        data_list = []
        resp = requests.get(api, headers=header)
        print (vars(resp))
        time.sleep(200)
        data = resp.text
        data_list.append(data)
        jsonData = resp.json()
        previousPage=""
        while(("next_page" in jsonData) and (jsonData["next_page"] is not None) and (jsonData["next_page"] is not previousPage)):
            previousPage = jsonData["next_page"]
            newapi = api+"&next_page="+jsonData["next_page"]
            print("API", newapi)
            resp = requests.get(newapi, headers=header)
            data = resp.text
            data_list.append(data)
            jsonData = resp.json()
        return data_list

