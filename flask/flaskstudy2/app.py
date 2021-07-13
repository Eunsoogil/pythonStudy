# pip install Flask-JWT
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
# token encrypt key
app.secret_key = 'jose'
api = Api(app)

# security.py에서 선언한 authenticate를 통해 비밀번호가 맞는지 확인함
# 그 다음 jwt가 토큰 발행
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# debug는 오류시 html로 알려줌
# app.py가 다른 python file로 import될때마다 구동되는 것을 방지하기 위해 추가,
# python app.py시에만 동작할 수 있도록 if문 추가
if __name__ == '__main__':
    app.run(port=1234, debug=True)
