from function import *

file_name = 'data/juso.txt'
def insert(name, phone, address):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{name},{phone},{address}")
        print("등록완료!")

while True:
    menuPrint("주소관리")
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1": #입력
        name = input("이름>")
        if name=="": continue
        phone = input("전화>")
        address = input("주소>")
        insert(name, phone, address)