import json 
from json2html import *
import requests
from files import File
from restapi import ApiHandler

class reports(File, ApiHandler):
    def __init__(self):
        File.__init__(self)
        ApiHandler.__init__(self, self.dataEndPoint, self.EndpointDataHeader)
    def generateReportData(self, file):
        '''This API go over the Data and generate the Data Based on Source IP.
        '''
        with open(file) as fp:
            data = json.load(fp)
        new_data={}
        result = []
        id = 0
        for ent in data["logs"]:
            if ent.get('ip') in new_data:
                my_dict=new_data[ent.get('ip')] 
                my_dict["ip"]=ent.get('ip')
                my_dict["count"]=my_dict["count"]+1
            else:
                id = id + 1
                new_data[ent.get('ip')] = {}
                my_dict={}
                my_dict["id"] = id
                my_dict["ip"]=ent.get('ip')
                my_dict["count"]=1
                my_dict["kind"] = ent.get("kind")
                my_dict["datetime"] =  ent.get('datetime')
                my_dict["metadata"] =  ent.get('metadata')
                #da = = self.getApiData(my_dict["ip"])
                da = self.getDataFromApi(self.ipEndpoint+my_dict["ip"], header=self.ipHeader)
                dat = json.loads(da)
                my_dict["metadata"]["resolved_ip"]["org"] = dat["org"]
                my_dict["metadata"]["resolved_ip"]["isp"] = dat["isp"]
                my_dict["metadata"]["resolved_ip"]["zip"] = dat["zip"] 
             
            
            new_data[ent.get('ip')].update(my_dict)
        for dict in new_data:
            dic_item = new_data[dict]
            result.append(dic_item)
        return result

    def generateHtml(self, file, data):
        '''This API go over the Data and generate the Data Based on Source IP.
        '''
        html = json2html.convert(json = data)
        with open(file, "w") as fp:
            fp.write(html)

if __name__ == "__main__":
    rp = reports()
    data = rp.getDataFromApi(rp.dataEndpoint+rp.dataEndPointFilter+rp.apiParam, header=rp.dataHeader)
    data=json.loads(data)
    rp.write(rp.fileName, data)
    rp.generateHtml(rp.htmlFileName, data)
    data = rp.generateReportData(rp.fileName)
    rp.generateHtml(rp.htmlReportName, data)
    rp.htmlFileToPdf()
    
