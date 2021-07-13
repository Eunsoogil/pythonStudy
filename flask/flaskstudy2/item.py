import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


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
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if items else 404

        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'item not found'}, 404

    def post(self, name):
        # body가 json이 아니면 error
        # force=True를 넣으면 json이 아니여도 강제로 형변환 시도
        # silent=True : json아니면 null
        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        #     return {'message': "item '{}' already exists".format(name)}, 400

        # parser로 체크한 값을 넘겨줌, Item class 하위
        # data = request.get_json(silent=True)

        if self.find_by_name(name):
            return {'message': "item '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201

    def delete(self, name):
        # 전역 변수 사용함을 알림
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

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

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}


class ItemList(Resource):
    def get(self):
        return {'items': items}