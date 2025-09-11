import os, pandas as pd
file_pro = '교수.csv'

def inputNum(title):
    while True:
        num = input(title)
        if num=='':
            return ''
        elif num.isnumeric():
            return int(num)
        else:
            print('숫자로 입력하세요!')

def pro_list():
    pro = pd.read_csv(file_pro, index_col='교수번호')
    for idx, row in pro.iterrows():
        print(idx, row['교수이름'], row['교수학과'], row['임용일'], end=' ')
        print(f'{row["급여"]:,} {row["교수직급"]}')

def pro_search(code):
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    if code in pro.index:
        pro_row = pro.loc[code]
        print(code, pro_row['교수이름'], pro_row['교수학과'])

        print('담당학생-------------------------')
        filt = stu['지도교수'] == code
        stu_rows = stu[filt]
        for idx, row in stu_rows.iterrows():
            print(idx, row['학생이름'], row['학생학과'])

        print('담당강좌--------------------------')
        filt = cou['담당교수'] == code
        cou_rows = cou[filt]
        for idx, row in cou_rows.iterrows():
            print(idx, row['강좌이름'], row['강의시수'])
    else:
        print('해당 교수가 없습니다.')

while True:
    os.system('cls')
    print('-' * 50)
    print('**** 학사관리 ****')
    print('-' * 50)
    print('[1]교수목록')
    print('[2]교수검색')
    print('[3]학생목록')
    print('[4]학생검색')
    print('[5]강좌목록')
    print('[6]강좌검색')
    print('[0]프로그램종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1':
        pro_list()
        input('아무키나 누르세요!')
    elif menu=='2':
        while True:
            code = inputNum('교수번호>')
            if code=='': break
            pro_search(code)