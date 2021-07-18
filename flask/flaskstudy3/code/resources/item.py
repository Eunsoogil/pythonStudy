from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field cannot be left black'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='every item needs a store id'
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "item '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "an error occurred inserting the item"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json(), 201


class ItemList(Resource):
    def get(self):
        # 2가지 방법 모두 좋음
        # return {'items': [item.json() for item in ItemModel.query.all()]}
        # 아래 방법이 더 효율이 좋다고 함 (확실하지는 않음)
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
