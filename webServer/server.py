from flask import Flask
from flask import render_template
# cmd : C:\path\to\app>set FLASK_APP=hello.py
# cmd : python -m flask run 또는 flask run
# cmd : set FLASK_ENV=development 시 디버그 모드 on, 수정할때마다 바꿀 필요 없음

app = Flask(__name__)
# print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
