# restapi.py
import requests
import json 
 

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
        data = kwargs.get('page', "")
        resp = requests.get(api, headers=header)
        data += resp.text
        if 'next' in resp.links.keys():
            return (getDataFromApi(resp.links['next']['url'], header,page=data))
        return (data)

