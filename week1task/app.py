from flask import Flask , render_template, Response, request, send_from_directory, make_response
import sys
import urllib.request, json
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    auth_data = json.loads(url.read().decode())
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as url:
    post_data = json.loads(url.read().decode())

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world Aakash'

@app.route('/html')
def html():
    return render_template('home.html')
'''
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/setcookie')
def setcookie():
    resp = make_response("Setting Cookie!")
    resp.set_cookie('aakash','bidlan')
    resp.set_cookie('age','12')
    return resp

@app.route('/getcookie')
def getcookie():
    cook1 = request.cookies.get('aakash')
    cook2 = request.cookies.get('age')
    return 'The name is '+cook1+ ' and age is '+cook2

@app.route("/author")
def auth():
    return render_template('author.html',data=auth_data)

@app.route("/post")
def posts():
    return render_template('post.html',data1=post_data)

@app.route('/count')
def task2c():
    tot = []

    for i in auth_data:
        totp = 0
        for j in post_data:
            if j["userId"] == i["id"]:
                totp += 1
        tot.append(totp)

    respstr = ""
    for i in auth_data:
        respstr += "Author: {}".format(i["name"])
        respstr += "</br>"

    respstr += "Total posts in order of the user"

    for i in range(0,10):
        respstr += "&nbsp"*5
        respstr += "</br>"
        respstr += "Total Posts: {}".format(tot[i])
    return respstr

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        sys.stdout.write(name)
        sys.stdout.flush()
        return render_template('name.html',name=name)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
