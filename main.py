import schedule
import time
import json
from report import reports
import sys
from settings import inputs
arg_list = ["-help", "main.py"]

def getDataAndGenerateReport():
    rp = reports()
    data_list = rp.getDataFromApi(rp.dataEndpoint+"?endtime="+rp.apiEndTime+"&&starttime="+rp.apiParam, header=rp.dataHeader)
    for data in data_list:
        data = json.loads(data)
        rp.write(rp.fileName, data)
        rp.generateHtml(rp.htmlFileName, data)
        reportdata, iplist, orglist, pullcountlist = rp.generateReportData(None, data)
        rp.generateHtml(rp.htmlReportName, reportdata)
        #rp.generateBarChart(iplist, orglist, pullcountlist)
    rp.htmlFileToPdf()

       
if __name__ == "__main__":
    help_flag = True
    for eachArg in sys.argv:
        if (eachArg not in arg_list):
            print("Invalid Command argument option please provide valid input")
            exit(0)
        if (("-help" in eachArg) and help_flag):
            help_flag = False
            print("This tool featches the logs from provided API and Generate report in HTML and PDF format\n")
    schedule.every().day.do(getDataAndGenerateReport)
    schedule.every(10).minutes.do(getDataAndGenerateReport)
    while True:
        schedule.run_pending()
        time.sleep(1)
