from werkzeug.security import safe_str_cmp
from user import User

# users = [
#     User(1, 'bob', '1234')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}
#
#
# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     # 아래 방식보다 safe_str_cmp가 더 안전(?)
#     # if user and user.password == password:
#     if user and safe_str_cmp(user.password, password):
#         return user
#
#
# def identity(payload):
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
