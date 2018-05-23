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


@app.route('/logs', methods=['POST', 'GET'])
def retrieve_logs_with_args():
    # order = 0
    # filter = 0
    # fileName = ""

    # if request.method == 'POST':
    #     if request.form.get('order'):
    #         order = request.form['order']
    #     if request.form.get('filter'):
    #         filter = request.form['filter']
    #     if request.form.get('fileName'):
    #         fileName = request.form['fileName']

    order = request.form.get('order', 0)
    filter = request.form.get('filter', 0)
    fileName = request.form.get('fileName', "")

    headings = ["Schema ID", "File ID", "Instance ID", "File Name", "Version Text", "Effective From", "Records Loaded", "User ID", "User Email", "PSU Status ID", "Started", "Ended"]

    logs = view_logs.get_all(order,filter, fileName)
    return render_template('view_logs.html', logs=logs, headings=headings)


if __name__ == '__main__':
    app.run(port='5001')