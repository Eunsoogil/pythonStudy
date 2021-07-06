# pip3.5 install flask
# jsonify => json handler
from flask import Flask, jsonify, request, render_template

# __name__ : unique name return
# app에 unique name을 등록하여 Flask에서 return, 일종의 등록
app = Flask(__name__)


# www.google.com에 접속하면 실제로는 www.google.com/ 이다
@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only


stores = [
    {
        'name': 'store1',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data:{name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<String:name>
# 파라미터를 아래와 같이 사용 가능
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    # stores가 리스트형태라 아래와같이 전송
    # json은 항상 " double quotes사용
    return jsonify({'stores': stores})


# POST /store/<String:name>/item {name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /store/<String:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def create_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# 포트 명시
app.run(port=1234)

# 실행할때 python3.5 app.py로 돌림

# 해당 폴더 디렉토리에서 (flaskstudy) python3.5 app.py 명령어 입력시 flask 돌아감

# 모듈 확인
# pip3.5 freeze

# 가상환경
# pip3.5 install virtualenv

# 새로운 파이썬을 깐다
# virtualenv venv --python=python3.5

# . venv/bin/activate

# deactivate

# pip install Flask-RESTful
