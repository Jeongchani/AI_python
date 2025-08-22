from function import *
from product import Product

products = [
    {'code':'001', 'name':'LG 냉장고', 'price':250},
    {'code':'002', 'name':'LG 세탁기', 'price':180},
]
while True:
    menuPrint("상품관리")
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1": #등록
        code = len(products)+1
        code = f'{code:03d}'
        print(f"상품코드>{code}")
        name = input("상품이름>")
        price = input("상품가격>")
        p = Product(code, name, price)
        products.append(p.dict())
        print("상품등록완료!")
    elif menu=="3": #목록
        for p in products:
            print(p['code'], p['name'], p['price'])
        print(f'{len(products)}개 상품이 존재합니다!')
    elif menu=="2": #검색
        name = input("검색이름>")
        for p in products:
            if p['name'].upper().find(name.upper()) != -1:
                print(p['code'], p['name'], p['price'])
    elif menu=="4": #삭제
        code = input("삭제코드>")
        if code == "":continue
        for idx, p in enumerate(products):
            if p['code'] == code:
                products.pop(idx)
                print("상품삭제완료!")
