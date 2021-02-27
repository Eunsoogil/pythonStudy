# python -m venv location
# location\Scripts\activate.bat  >> 실행하면 콘솔 () 부분이 location으로 바뀜
# pip --version으로 virtual environment 확인
# pip install Flask
# d:\pythonstudy\webserver\venv\scripts\python.exe -m pip install --upgrade pip pip 업그레이드 하라고 나옴

from flask import Flask, render_template, url_for, request, redirect
import csv

# cmd : C:\path\to\app>set FLASK_APP=hello.py
# cmd : python -m flask run 또는 flask run
# cmd : set FLASK_ENV=development 시 디버그 모드 on, 수정할때마다 바꿀 필요 없음

# mashup에서 universe 템플릿 받음

app = Flask(__name__)


# print(__name__)


# @app.route('/')
# def hello_world():
#     return render_template('index.html')
#
#
# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/<username>/<int:post_id>')
# def usernameRender(username=None, post_id=None):
#     # post_id의 경우 int형이 아니면 안됨(404)
#     return render_template('index.html', name=username, post_id=post_id)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    if page_name == 'favicon.ico':
        return url_for('static', filename='favicon.ico')
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # dictionary data type으로
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'did not save to database'
    else:
        return redirect('/contact.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):  # csv : comma separate value
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# pythonanywhere
# python 파일만 넘기고 pip freeze > requirements.txt (또는 pip3) 하면 module 저장
# git에 올리고 https 주소 복사후 pythonanywhere dashboard에 console > bash > 리눅스 서버 들어감 > git clone 주소
# pythonanywhere web tap에 들어가서 하나 만들기 (flask 말고 manual configuration)
# 배포 후 code 부분에 파일 주소 (ex. web_portfo)
# 다시 bash 가서
# mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv
# pip install flask
# workon my-virtualenv
# cd 로 들어가서
# pip install -r requirements.txt
