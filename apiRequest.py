#does this need to be in its own python file??
#did I name it appropriately?
import requests
import zipfile
import json
import io
import csv 
import sys

# Setting user Parameters
apiToken = "WGdn1H9V3oCPwtznLPMlQ06I9J1lCd4Zlqacu9QU"
surveyId = "SV_88F5xJ8pHg7QKVv"
fileFormat = "csv" #should this be 'csv?'
dataCenter = 'ca1' 

# Setting static parameters
requestCheckProgress = 0
progressStatus = "in progress"
baseUrl = "https://{cuboulder.ca1}.qualtrics.com/API/v3/responseexports/".format(dataCenter)
headers = {
    "content-type": "application/csv",
    "x-api-token": WGdn1H9V3oCPwtznLPMlQ06I9J1lCd4Zlqacu9QU,
    }

# Step 1: Creating Data Export
downloadRequestUrl = baseUrl
downloadRequestPayload = '{"format":"' + fileFormat + '","surveyId":"' + surveyId + '"}'
downloadRequestResponse = requests.request("POST", downloadRequestUrl, data=downloadRequestPayload, headers=headers)
progressId = downloadRequestResponse.csv()["result"]["id"]#does this need to be changed?
print(downloadRequestResponse.text)

# Step 2: Checking on Data Export Progress and waiting until export is ready

isFile = None

while requestCheckProgress < 100 and progressStatus is not "complete" and isFile is None:
    requestCheckUrl = baseUrl + progressId
    requestCheckResponse = requests.request("GET", requestCheckUrl, headers=headers)
    isFile = (requestCheckResponse.json()["result"]["file"])#does this need to say json?
    if isFile is None:
       print ("file not ready")
    else:
       print ("file created:", requestCheckResponse.json()["result"]["file"])#and this too?
    requestCheckProgress = requestCheckResponse.json()["result"]["percentComplete"]
    print("Download is " + str(requestCheckProgress) + " complete")

# Step 3: Downloading file
requestDownloadUrl = baseUrl + progressId + '/file'
requestDownload = requests.request("GET", requestDownloadUrl, headers=headers, stream=True)

# Step 4: Unzipping the file
zipfile.ZipFile(io.BytesIO(requestDownload.content)).extractall("MyQualtricsDownload")
print('Complete')