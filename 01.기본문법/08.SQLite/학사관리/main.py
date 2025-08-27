from function import *
from database import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print('프로그램을 종료합니다.')
        break
    elif menu=='1':
        pass
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='':break
            students = search(value)
            if len(students)==0:
                print('검색결과가 없습니다.')
                continue
            for stu in students:
                stu.print()
            print(f'{len(students)}명 학생이 존재합니다.') 
    elif menu=='3':
        students = list()
        for stu in students:
            stu.print()
        print(f'{len(students)}명 학생이 존재합니다.')    
    elif menu=='4':
        pass
    elif menu=='5':
        pass
    else:
        print('0~5번 메뉴를 선택하세요!')    