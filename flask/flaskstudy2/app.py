# pip install Flask-JWT
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
# token encrypt key
app.secret_key = 'jose'
api = Api(app)

# security.py에서 선언한 authenticate를 통해 비밀번호가 맞는지 확인함
# 그 다음 jwt가 토큰 발행
jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    # Item class 내의 변수식으로 사용
    # price만 있는지 확인하기 위해 사용
    parser = reqparse.RequestParser()

    # price외에는 추가할 수 없다
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field cannot be left black'
                        )

    # 먼저 실행
    # JWT access_token 식으로 헤더에 넣어서 요청
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item

        # 위와 동일한 동작, next의 경우 1개만 return
        # None의 경우 items가 비어있을때 default return value
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if items else 404

    def post(self, name):
        # body가 json이 아니면 error
        # force=True를 넣으면 json이 아니여도 강제로 형변환 시도
        # silent=True : json아니면 null
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "item '{}' already exists".format(name)}, 400

        # parser로 체크한 값을 넘겨줌, Item class 하위
        # data = request.get_json(silent=True)
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        # 전역 변수 사용함을 알림
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item is deleted'}

    def put(self, name):
        # parser로 체크한 값을 넘겨줌, Item class 하위
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# debug는 오류시 html로 알려줌
app.run(port=1234, debug=True)
