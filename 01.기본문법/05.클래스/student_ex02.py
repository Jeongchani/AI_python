from student import Student

students = []
while True:
    print('----------------------')
    print('|1.등록|2.목록|0.종료|')
    print('----------------------')
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1":
        s = Student()
        s.no = input("번호>")
        s.name = input("이름>")
        students.append(s.info())
    elif menu=="2":
        for s in students:
            stu = Student()
            stu.no = s['no']
            stu.name = s['name']
            stu.info_print()