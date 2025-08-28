from function import *
from db import *

while True:
    menuPrint('학사관리')
    menu=input('메뉴선택>')
    if menu=='0':
        cur.close()
        con.close()
        print('프로그램을 종료합니다!')
        break
    elif menu=='1':
        stu = Student()
        stu.id = newID()
        print(f'학생학번>{stu.id}')
        stu.name = input('학생이름>')
        if stu.name=='':
            print('학생이름은 꼭 입력하세요!')
            continue
        stu.code = inputCode('학생학과>', 1)
        insert(stu)
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='': break
            students = search(value)
            if len(students)==0:
                print('검색학생이 없습니다.')
            else:
                for stu in students:
                    stu.print()
    elif menu=='3':
        while True:
            key = inputNum('1.학번순|2.이름순|3.학과순>')
            if key=='':
                break
            elif key<1 or key>3:
                print('1~3 숫자를 입력하세요!')
                continue
            students = list(key)
            for stu in students:
                stu.print()
    elif menu=='4':
        id = input('학생번호>')
        if id=='':continue
        stu = read(id)
        if stu==None:
            print('삭제할 학생이 없습니다!')
        else:
            stu.print()
            sel = input('삭제하실래요(Y)>')
            if sel=='Y' or sel=='y':
                delete(id)
    elif menu=='5':
        pass
    else:
        print('0~5번 숫자를 선택하세요!')
