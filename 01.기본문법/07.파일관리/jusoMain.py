from function import *
from jusoFile import *

def newSeq(): #새로운 번호를 리턴함수
    list = fileRead()
    if len(list)==0: return 1
    seqs = [p.seq for p in list]
    return max(seqs)+1

def searchSeq(seq):
    list = fileRead()
    result = [p for p in list if p.seq==seq]
    if len(result) > 0: return result[0]

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu=="0":
        print("프로그램을 종료합니다.")
        break
    elif menu=="1": #입력
        person = Person()
        person.seq = newSeq()
        print(f"번호>{person.seq}")
        if person.seq == '': continue
        person.name = input("이름>")
        if person.name == '': continue
        person.address = input('주소>')
        fileAppend(person)
        person.print()
    elif menu=="3": #목록
        list = fileRead()
        for person in list:
            person.print()
    elif menu=="4": #삭제
        seq = inputNum("삭제번호>")
        list = fileRead()
        result = [p for p in list if p.seq==seq]
        if len(result)==0:
            print("삭제할 번호가 없습니다.")
            continue
        person = result[0]
        person.print()
        sel = input('삭제하실래요(Y)>')
        if sel == 'Y' or sel=='y':
            result = [p for p in list if p.seq!=seq]
            fileWrite(result)
            print("삭제성공!")