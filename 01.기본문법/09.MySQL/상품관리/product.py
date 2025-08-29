from db import *
from classes import *

def list():
    try:
        sql = 'select * from product'
        cur.execute(sql)
        rows = cur.fetchall()
        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']
            products.append(product)
        return products
    except Exception as err:
        print('상품목록오류:', err)

def insert(product):
    try:
        sql = 'insert into product(code, name, price) values(%s, %s, %s)'
        cur.execute(sql, (product.code, product.name, product.price))
        con.commit()
        print('상품등록완료!')
    except Exception as err:
        print('상품등록오류:', err)

def search(value):
    try:
        sql ='select * from product where code like %s or name like %s'
        cur.execute(sql, (f'%{value}%', f'%{value}%'))
        rows = cur.fetchall()
        if rows != None:
            products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.price = row['price']
                products.append(product)
            return products
    except Exception as err:
        print('상품검색오류:', err)

def read(code):
    try:
        sql = f'select * from product where code={code}'
        cur.execute(sql)
        row = cur.fetchone()
        if row != None:
            product = Product()
            product.code=row['code']
            product.name=row['name']
            product.price=row['price']
            return product
    except Exception as err:
        print('상품읽기오류:', err)

def inputCode():
    while True:
        code = input('상품코드>')
        if code=='': return code
        if len(code) !=3:
            print('상품코드는 3자리로 입력하세요!')
        elif not code.isnumeric():
            print('상품코드는 숫자로 입력하세요!')
        else:
            pro = read(code)
            if pro != None:
                pro.print()
                print('이미 등록된 상품입니다.')
            else:
                return code
            
def inputPrice(title):
    while True:
        price = input(title)
        if price=='':
            return ''
        elif not price.isnumeric():
            print('가격은 숫자로 입력하세요!')
        else:
            return int(price)

def update(product):
    try:
        sql = 'update product set name=%s, price=%s where code=%s'
        cur.execute(sql, (product.name, product.price, product.code))
        con.commit()
        print('상품수정완료!')
    except Exception as err:
        print('상품수정오류:', err)

if __name__=='__main__':
    price = inputPrice('상품가격>')
    print('가격:', price)