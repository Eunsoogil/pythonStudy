# pip install Flask-JWT
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
# token encrypt key
app.secret_key = 'jose'
api = Api(app)

items = []


class Item(Resource):
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

        data = request.get_json(silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# debug는 오류시 html로 알려줌
app.run(port=1234, debug=True)
