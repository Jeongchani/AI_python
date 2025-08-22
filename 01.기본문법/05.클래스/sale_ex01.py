from function import *
from product import Product
from sale import Sale

products = [
    {'code':'001', 'name':'LG 냉장고', 'price':250},
    {'code':'002', 'name':'LG 세탁기', 'price':180},
]

sale = []

def search(code):
    for p in products:
        if code==p['code']:
            return p
        
while True:
    menuPrint('매출관리')
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1": #등록
        code = input("상품코드>")
        if code=="": continue
        p = search(code)
        if p==None:
            print(f"{code}번 상품이 없습니다.")
        else:
            name = p['name']
            price =p['price']
            print(f'상품명:{name}, 가격:{price}')
            qnt = inputNum("수량>")
            if qnt=="":continue
            s = Sale(code, name, price, qnt)
            sale.append(s.dict())
            print("매출등록완료!")
    elif menu=="3": #목록
        for s in sale:
            print(f"{s['code']},{s['name']},{s['price']:,}만원,", end="")
            print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
