from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # lazy='dynamic'을 넣으면 한번 객체 생성시 미리 정보를 저장해놓지 않는다
    # 아이템이 많은 경우에는 객체를 한 번 생성할때마다 모든 정보를 불러와야하므로 비용이 많이든다
    # 다만, 이렇게 되면 아래 json 메소드처럼 items를 조회할때는 매번 DB를 호출해야하기 때문에 느리다
    # 장단이 있음
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
