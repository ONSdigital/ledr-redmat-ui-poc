from flask import Flask, render_template, request, redirect
import auth
import view_logs

app = Flask(__name__)


@app.route('/')
def login_screen():
    return render_template('index.html')


@app.route('/menu')
def menu_screen():
    return render_template('menu.html')


@app.route('/auth', methods=['POST'])
def auth_check():
    user = request.form['user']
    password = request.form['password']

    if auth.login(user, password) == 1:
        return redirect('/menu')
    else:
        return redirect('/')


@app.route('/logs')
def retrieve_logs():

    headings = ["Schema ID", "File ID", "Instance ID", "File Name", "Version Text", "Effective From", "Records Loaded", "User ID", "User Email", "PSU Status ID", "Started", "Ended"]

    logs = view_logs.get_all()
    return render_template('view_logs.html', logs=logs, headings=headings)


if __name__ == '__main__':
    app.run()