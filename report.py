import json 
from json2html import *
import requests
from files import File
from restapi import ApiHandler
import numpy as np
import matplotlib.pyplot as plt


class reports(File, ApiHandler):
    def __init__(self):
        File.__init__(self)
        ApiHandler.__init__(self, self.dataEndPoint, self.EndpointDataHeader)
    def generateReportData(self, file, data):
        '''This API go over the Data and generate the Data Based on Source IP.
        '''
        data_list = []
        if (file is not None):
            with open(file) as fp:
               data_list.append(json.loads(fp))
        else:
            data_list.append(data)
        new_data={}
        result = []
        iplist = []
        orglist = []
        pullcountlist = []
        id = 0
        for data in data_list:
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
                   for data in da:
                      dat = json.loads(data)
                   my_dict["metadata"]["resolved_ip"]["org"] = dat["org"]
                   my_dict["metadata"]["resolved_ip"]["isp"] = dat["isp"]
                   my_dict["metadata"]["resolved_ip"]["zip"] = dat["zip"] 
                   new_data[ent.get('ip')].update(my_dict)

        for dict in new_data:
            dic_item = new_data[dict]
            iplist.append(dic_item["ip"])
            orglist.append(dic_item["metadata"]["resolved_ip"]["org"])
            pullcountlist.append(dic_item["count"])
            result.append(dic_item)
        return result, iplist, orglist, pullcountlist

    def generateHtml(self, file, data):
        '''This API go over the Data and generate the Data Based on Source IP.
        '''
        #with open(srcfile, 'r') as fobj:
        #     data = json.load(fobj)
        html = json2html.convert(json = data)
        with open(file, "a") as fp:
            fp.write(html)
    def generateBarChart(self, iplist, orglist, pullcountlist):
        '''This API go over the Data and generate the Data Based on Source IP.
        '''
        width = 0.25
        fig, ax = plt.subplots()
        rects = ax.bar(iplist, pullcountlist, width, color='b', align='center')
        ax.set_title('CIC Download Stats '+self.time)
        ax.set_ylabel('Download Counts')
        ax.set_xlabel('Client IP Address')
        ax.set_xticklabels(iplist)
        #ax.set_yticklabels(range(0, (max(pullcountlist)+10), 2))
        i = 0
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % str(orglist[i]),
                ha='center', va='bottom')
            i = i + 1
        plt.savefig(self.pdfChartName)
    def appendChartWithHtml(self, chart, html):
        for element in chart.body:
            html.body.append(element)
    def appendPdfs(self, src, dst):
        from pdfrw import PdfReader, PdfWriter
        new_pdf = PdfWriter()
        x = PdfReader(src)
        y = PdfReader(dst)
        new_pdf.addpage(x.pages[0])
        print("Janraj")
        new_pdf.addpage(y.pages[0])
        print("CJ")
        new_pdf.write("result.pdf")
	
        #for inpfn in dst:
        #    writer.addpages(PdfReader(inpfn).pages)
        #writer.write(src)

        #for element in chart.body:
        #    html.body.append(element)

if __name__ == "__main__":
    rp = reports()
    data_list = rp.getDataFromApi(rp.dataEndpoint+rp.dataEndPointFilter+rp.apiEndTime+"&starttime="+rp.apiParam, header=rp.dataHeader)
    for data in data_list:
        data = json.loads(data)
        rp.write(rp.fileName, data)
        rp.generateHtml(rp.htmlFileName, data)
        reportdata, iplist, orglist, pullcountlist = rp.generateReportData(None, data)
        rp.generateHtml(rp.htmlReportName, reportdata)
        #rp.generateBarChart(iplist, orglist, pullcountlist)
    rp.htmlFileToPdf()
    
