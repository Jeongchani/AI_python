#1.남탕: 남자이거나 여자이면서 나이가 4세미만
#2.여탕: 여자이거나 남자이면서 나이가 4세미만
while True:
    type = input("1.남탕|2.여탕|0.종료>")
    if type == "0":
        print("프로그램을 종료합니다.")
        break
    elif type=="1" or type=="2":
        gender = input("1.남자|2.여자>")
        if type=="1": #남탕
            if gender == "1": #남자
                print("남자이므로 남탕입장이 가능합니다.")
            else:#여자
                age = int(input("나이>"))
                if age < 4:
                    print("여자지만 4세미만이므로 남탕에 입장이 가능합니다.")
                else:
                    print("여자이고 4세이상이므로 남탕에 입장이 불가능합니다.")    
        else: #여탕
            pass
    else:
        print("0~2 숫자를 입력하세요.")