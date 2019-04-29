import time
import requests
import json 
from json2html import *
import pdfkit
from datetime import datetime
from datetime import timedelta
from settings import inputs

class File(inputs):
    def __init__(self):
        inputs.__init__(self)
        self.time = self.getTime()
        self.fileName = self.getFileName("","json")
        self.apiParam = self.getApiParam()
        self.apiEndTime = self.getApiEndtime()
        self.htmlFileName = self.getFileName("","html")
        self.htmlReportName   = self.getFileName("_report","html")
        self.pdfFileName = self.getFileName("_report","pdf")
        self.pdfChartName = self.getFileName("_chart","pdf")
    def getApiParam(self):
        start_time = ((datetime.now() - timedelta(days=7)))
        return start_time.strftime("%m/%d/%Y") 
    def getApiEndtime(self):
        return time.strftime("%m/%d/%Y") 
    def getTime(self):
        return time.strftime("%m-%d-%Y")
    def getFileName(self, prefix, ext):
        return self.outputFile+"_"+self.time+prefix+"."+ext
    def write(self, filename, data):
        with open(filename, 'a') as outfile:
            json.dump(data, outfile)
    def htmlFileToPdf(self):
        with open(self.htmlReportName) as fp:
            pdfkit.from_file(fp, self.pdfFileName)


if __name__ == "__main__":
    FileObj = File()
    print("File Object Deatils\n {}\n".format(vars(FileObj)))
    
