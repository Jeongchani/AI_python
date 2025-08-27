from function import *
from database import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print('프로그램을 종료합니다.')
        cur.close()
        con.close()
        break
    elif menu=='1':
        stu = Student()
        stu.id = newID()
        print(f'학번>{stu.id}')
        while True:
            stu.name = input('이름>')
            if stu.name == '':
                print('이름은 반드시 입력하세요!')
                continue
            else:
                break
        while True:
            depts = listDept()
            for dept in depts:
                print(f'{dept.code}.{dept.name}', end='|')
            stu.dept = inputNum('학과>')
            if stu.dept <1 or stu.dept >3:
                print('학과코드는 1~3을 입력하세요!')
                continue
            else:
                break
        insert(stu)
        print('학생등록성공!')

    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='':break
            students = search(value)
            if students==None:
                print('검색결과가 없습니다.')
                continue
            for stu in students:
                stu.print()
            print(f'{len(students)}명 학생이 존재합니다.\n') 
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