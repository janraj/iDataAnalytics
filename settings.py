# settings.py
import os
from dotenv import load_dotenv

class inputs(object):
    def __init__(self):
        load_dotenv()
        self.EndpointDataHeader = {'content-type': 'application/json'} 
        self.dataEndPoint = os.getenv("DATA_ENDPOINT")
        self.dataEndPointFilter = os.getenv("DATA_ENDPOINT_FILTER_TODAY")
        self.dataEndpointKey = os.getenv("DATA_ENDPOINT_KEY")
        self.outputFile = os.getenv("OUTPUT_FILE_NAME")
        self.EndpointDataHeader.update({"Authorization": self.dataEndpointKey})
