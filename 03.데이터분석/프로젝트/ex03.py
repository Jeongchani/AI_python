import os
import pandas as pd

file_name = 'c:/python/03.데이터분석/data/학생성적.csv'
score = pd.read_csv(file_name)
cols = score.columns

while True:
    os.system('cls')
    print('-' * 50)
    print('**************** 성 적 관 리 *****************')
    print('-' * 50)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1':#등록
        index = max(score.index)+1
        no = score['지원번호'].max()+1
        grade=[]
        for col in cols:
            num = input(f'{col}>')
            
        input('아무키나 누르세요!')
    elif menu=='2': #목록
        for idx in range(len(score)):
            row = score.loc[idx]
            for col in cols:
                print(f'{col}:{row[col]}', end=' ')
            print()
        input('아무키나 누르세요!')
    elif menu=='3':
        input('아무키나 누르세요!')
    elif menu=='4':
        input('아무키나 누르세요!')
    elif menu=='5':
        input('아무키나 누르세요!')
    else:
        input('0~5번 메뉴를 선택하세요!')