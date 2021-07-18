# pip install Flask-JWT
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# 켜놓으면 session에서 발생하는 모든 modification을 기록하나 성능에 좋지 않고 다른 방법이 있음
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# token encrypt key
app.secret_key = 'jose'
api = Api(app)


# app.config['SQLALCHEMY_DATABASE_URI'] 에 table이 없으면 만들고 있으면 안만든다
# 반드시 필요한 모델을 import 해야함
@app.before_first_request
def create_tables():
    db.create_all()

# security.py에서 선언한 authenticate를 통해 비밀번호가 맞는지 확인함ß
# 그 다음 jwt가 토큰 발행
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# debug는 오류시 html로 알려줌
# app.py가 다른 python file로 import될때마다 구동되는 것을 방지하기 위해 추가,
# python app.py시에만 동작할 수 있도록 if문 추가
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=1234, debug=True)
