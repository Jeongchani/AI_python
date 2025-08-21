from function2 import *

sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

while True:
    menuPrint("상품관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료합니다.")
        break
    elif menu == "1": #입력
        pass
    elif menu == "2": #검색
        code = inputNum("검색코드>")
        idx = search(sale, code)
        if idx == None:
            print(f'{code}번 상품이 없습니다.')
        else:
            s = sale[idx]
            print(f"상품이름:{s['name']}")
            print(f"상품가격:{s['price']:,}만원")
            print(f"판매수량:{s['qnt']:,}개")    
            print(f"총매출가:{s['price']*s['qnt']:,}만원")
    elif menu == "3": #목록
        pass
    elif menu == "4": #삭제
        pass
    elif menu == "5": #수정
        pass
    else:
        print("0~5를 입력하세요!")                