import requests
from requests.auth import HTTPDigestAuth
import json


def get_all(order, filter, fileName):
    url = "http://localhost:8126/log/"

    if filter:
        url = url + fileName
    if order:
        url = url + "?order=true"
    else :
        url = url + "?order=false"

    print(url)

    logs = []
    response = requests.get(url, auth=HTTPDigestAuth("C##LEDRRDM: ", "ledrrdm: "), verify=True)  # TODO: remove auth

    if response.ok:
        data = json.loads(response.content)
        print(data)
        for log in data:
            logStr = []
            logStr.append(log["schemaId"])
            logStr.append(str(log["fileId"]))
            logStr.append(str(log["instanceId"]))
            logStr.append(str(log["fileName"]))
            logStr.append(str(log["versionText"]))
            logStr.append(str(log["effectiveFrom"]))
            logStr.append(str(log["recordsLoaded"]))
            logStr.append(str(log["userId"]))
            logStr.append(str(log["userEmail"]))
            logStr.append(str(log["psuStatusId"]))
            logStr.append(str(log["started"]))
            logStr.append(str(log["ended"]))

            logs.append(logStr)
    else:
        response.raise_for_status()

    return logs
