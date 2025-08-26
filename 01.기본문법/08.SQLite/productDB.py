import os
import sqlite3
path =os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Product:
    def __init__(self):
        self.code=0
        self.name=''
        self.price=0

    def print(self):
        print(f'코드:{self.code}, 이름:{self.name}, 가격:{self.price:,}원')   

def list(type): #type=1:코드순, 2:이름, 3:최저가, 4:최고가
    con = sqlite3.connect(db_name) #데이터베이스 오픈
    cursor=con.cursor() #커서 오픈
    sql='select * from product '
    if type==1:
        sql +='order by code'
    elif type==2:
        sql +='order by name'
    elif type==3:
        sql +='order by price'
    elif type==4:
        sql +='order by price desc'        
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

def list_test(type):
    rows = list(type)
    for row in rows:
        p = Product()
        p.code = row[0]
        p.name = row[1]
        p.price = row[2]
        p.print()

if __name__=='__main__':
    list_test(4)