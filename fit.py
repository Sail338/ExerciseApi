from apiclient.discovery import build

import httplib2 
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client import client
import json
import os.path
def auth():
    flow = flow_from_clientsecrets('client2.json',
        scope='https://www.googleapis.com/auth/fitness.activity.read',
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')


    uri = flow.step1_get_authorize_url()
    print uri
    cred = input("Enter shit ")
    step2 = flow.step2_exchange(cred)
    token = step2.to_json()
    print token

    with open("refresh.json",'w') as outfile:
        json.dump(token,outfile)


    with open('refresh.json') as json_data:
         d = json.dumps(json_data)
         cred = client.OAuth2Credentials.fromJson(d)
         kek = cred.authorize(http)
         
         fit = build('fitness','v1',http=kek)
if os.path.isfile('refresh.json') == False:
        auth()
def walk():
    #run normal authorization if token is already there
    with open('refresh.json') as json_data:
            d = json.load(json_data)
            cred = client.OAuth2Credentials.from_json(d)
            if cred.access_token_expired:
                auth()
    http_auth = cred.authorize(httplib2.Http())
    fit = build('fitness','v1',http=http_auth)

    body = {
        "aggregateBy": [
            {
                "dataSourceId": "raw:com.google.step_count.delta:com.bidusoft.plexfit:",
                "dataTypeName": "com.google.step_count.delta" 
                },
            ],
        "endTimeMillis": "1457238625000",
        "bucketBySession": {
            "minDurationMillis": "10", # Only sessions of duration longer than this is used
            },

        "startTimeMillis": "1456876800000", # required time range
       }
    user = fit.users()
    dat = fit.users().dataset().aggregate(userId ='me', body = body).execute()
    src =user.dataSources()
    dat = json.dumps(dat)
    dat = json.loads(dat)
    total_data = 0
    for i in dat['bucket']:
        for x in i['dataset']:
            for j in x['point']:
                for k in j['value']:
                    print k['intVal']
                    total_data += int(k['intVal'])
    return total_data 


x = walk()

