import os
from product import *

while True:
    os.system('cls')
    print('-----------------------')
    print('       상품관리          ')
    print('-----------------------')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품정보수정')
    print('[5] 매출관리')
    print('[0] 프로그램종료')
    print('-----------------------')
    menu = input('메뉴선택>')
    if menu=='0':
        cur.close()
        con.close()
        print('프로그램을 종료합니다.')
        break
    elif menu=='1':
        pro = Product()
        pro.code = inputCode()
        if pro.code=='':continue
        pro.name = input('상품이름>')
        pro.price = inputPrice('상품가격>')
        if pro.price == '': pro.price=0
        insert(pro)
        input('아무키나 누르세요!')
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='': break
            products = search(value)
            if len(products)==0:
                print('검색한 상품이 없습니다!')
            else:
                for product in products:
                    product.print()
    elif menu=='3':
        products = list()
        for product in products:
            product.print()
        input('아무키나 누르세요!')
    elif menu=='4':
        code = input('상품코드>')
        product = read(code)
        if product==None:
            print('수정할 상품이 없습니다.')
        else:
            name = input(f'상품이름:{product.name}>')
            if name != '': product.name=name
            price = inputPrice(f'상품가격:{product.price}>')
            if price!= '': product.price=price
            update(product)
        input('아무키나 누르세요!')
    elif menu=='5':
        input('아무키나 누르세요!')
    else:
        print('[0]~[5]번 메뉴를 선택하세요!')                                