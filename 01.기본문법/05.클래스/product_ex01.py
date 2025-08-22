from function import *
from product import Product

products = [
    {'code':'P001', 'name':'LG 냉장고', 'price':250},
    {'code':'P002', 'name':'LG 세탁기', 'price':180},
]
while True:
    menuPrint("상품관리")
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1": #등록
        code = len(products)+1
        code = f'P{code:03d}'
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
