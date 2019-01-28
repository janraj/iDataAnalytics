import time
import requests
import json 
from json2html import *
import pdfkit
from settings import inputs

class File(inputs):
    def __init__(self):
        inputs.__init__(self)
        self.time = self.getTime()
        self.fileName = self.getFileName("","json")
        self.apiParam = self.getApiParam()
        self.htmlFileName = self.getFileName("","html")
        self.htmlReportName   = self.getFileName("_report","html")
        self.pdfFileName = self.getFileName("_report","pdf")
    def getApiParam(self):
        return time.strftime("%d%m%Y") 
    def getTime(self):
        return time.strftime("%d-%m-%Y")
    def getFileName(self, prefix, ext):
        return self.outputFile+"_"+self.time+prefix+"."+ext
    def write(self, filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
    def htmlFileToPdf(self):
        with open(self.htmlReportName) as fp:
            pdfkit.from_file(fp, self.pdfFileName)


if __name__ == "__main__":
    FileObj = File()
    print("File Object Deatils\n {}\n".format(vars(FileObj)))
    
