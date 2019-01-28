import json
from report import reports
import sys
from settings import inputs
arg_list = ["-help", "main.py"]


       
if __name__ == "__main__":
    help_flag = True
    for eachArg in sys.argv:
        if (eachArg not in arg_list):
            print("Invalid Command argument option please provide valid input")
            exit(0)
        if (("-help" in eachArg) and help_flag):
            help_flag = False
            print("This tool featches the logs from provided API and Generate report in HTML and PDF format\n")

    rp = reports()
    data = rp.getDataFromApi(rp.dataEndpoint+"?starttime="+rp.apiParam, header=rp.dataHeader)
    data=json.loads(data)
    rp.write(rp.fileName, data)
    rp.generateHtml(rp.htmlFileName, data)
    data = rp.generateReportData(rp.fileName)
    rp.generateHtml(rp.htmlReportName, data)
    rp.htmlFileToPdf()
