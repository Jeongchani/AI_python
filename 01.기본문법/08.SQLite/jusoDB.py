import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Person:
    def __init__(self):
        self.seq = 0
        self.name = '홍길동'
        self.address = '경기도 광명시'

    def print(self):
        print(f'번호:{self.seq}, 이름:{self.name}, 주소:{self.address}')

#목록
def list():
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'select seq, name, address from juso'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

def read(value):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where name like ? or address like ?"
    value = f'%{value}%'
    cursor.execute(sql, (value, value,))
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

if __name__=='__main__':
    rows = read('홍')
    for row in rows:
        p = Person()
        p.seq = row[0]
        p.name = row[1]
        p.address = row[2]
        p.print()
