# sqlite : 로컬 저장용
# RDBMS 연결 목적이 아니다
# 실행 : python sqltest1.py
# 앱 실행의 경우 flaskstudy2 폴더에서 실행해야한다 ex) python flaskstudy2/app.py
# 하위로 이동 후 실행하면 db를 찾지 못함
import sqlite3

connection = sqlite3.connect('data.db')

# cursor: 쿼리를 실행하고 저장하는 목적
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', '1234')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

cursor.close()
