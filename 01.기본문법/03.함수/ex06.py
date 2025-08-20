from function import menuPrint, inputNum, grade

scores = []
while True:
    menuPrint("성적관리")
    menu = input("메뉴선택>")
    if menu=="0":
        print("프로그램을 종료합니다.")
        break
    elif menu=="1": #입력
        name= input("이름>")
        kor = inputNum("국어")
        eng = inputNum("영어")
        mat = inputNum("수학")
        scores.append({"name":name, "kor":kor, "eng":eng, "mat":mat})
        print("입력성공!")
    elif menu=="3": #목록
        for s in scores:
            tot = s['kor']+s['eng']+s['mat']
            avg = tot/3
            print(name, kor, eng, mat, f"{avg:.2f}", grade(avg))