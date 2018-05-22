from flask import Flask, render_template, request, redirect
import requests #REMOVE AND USE FLASK
from requests.auth import HTTPDigestAuth
import json
import login

app = Flask(__name__)


@app.route('/')
def login_screen():
    return render_template('index.html')


@app.route('/menu', methods=['POST'])
def menu_screen():
    user = request.form['user']
    password = request.form['password']
    print(password)
    if login.login(user, password) == 1:
        return render_template('menu.html')
    else:
        return render_template('index.html')


@app.route('/logs')
def log_screen():
    url = "http://localhost:8125/log/"
    logs = []
    headings = ["Schema ID", "File ID", "Instance ID", "File Name", "Version Text", "Effective From", "Records Loaded", "User ID", "User Email", "PSU Status ID", "Started", "Ended"]
    response = requests.get(url, auth=HTTPDigestAuth("C##LEDRRDM: ", "ledrrdm: "), verify=True)  # TODO: remove auth

    if(response.ok):
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
    return render_template('view_logs.html', logs=logs, headings=headings)

if __name__ == '__main__':
    app.run()


