from function import *
from productDB import *

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print("프로그램을 종료합니다.")
        break
    elif menu=='1':
        pass
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='':break
            rows = search(value)
            for row in rows:
                rowPrint(row)
    elif menu=='3':
        while True:
            type=inputNum('1.코드순|2.상품이름순|3.최저가|4.최고가>')
            if type=='':break
            rows = list(type)
            for row in rows:
                rowPrint(row)
    elif menu=='4':
        pass
    elif menu=='5':
        pass