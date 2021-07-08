# sqlite : 로컬 저장용
# RDBMS 연결 목적이 아니다
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
cursor.close()
