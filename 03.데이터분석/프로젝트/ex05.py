import os
import pandas as pd

file_score ='c:/python/03.데이터분석/data/학생성적.csv'
file_info ='c:/python/03.데이터분석/data/학생정보.csv'

def inputNum(title):
    while True:
        num = input(title)
        if num=='':
            return ''
        elif not num.isnumeric():
            print('점수는 숫자로입력하세요.')
        else:
            return int(num)
        
def submenu():
    while True:
        score = pd.read_csv(file_score, index_col='지원번호')
        info = pd.read_csv(file_info, index_col='지원번호')
        df = info.join(score)
        df.fillna(0, inplace=True)
        cols = ['국어', '영어', '수학', '사회', '과학']

        os.system('cls')
        print('-' * 50)
        print('***************** 성  적  관  리 ***************')
        print('-' * 50)
        print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
        print('-' * 50)
        menu = input('메뉴선택>')
        if menu=='0':
            break
        elif menu=='1': #등록
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록되지 않은 지원번호입니다.')
            elif no in score.index:
                print('이미 성적이 등록되었습니다.')
            else:
                row = info.loc[no]
                print(f'이름:{row["이름"]}')
                grade=[]
                for col in cols:
                    num = inputNum(f'{col}>')
                    if num=='': num=0
                    grade.append(num)
                score.loc[no] = grade
                score.to_csv(file_score)
                print('등록완료!')    
            input('아무키나 누르세요!')
        elif menu=='2': #목록
            for idx in df.index:
                row = df.loc[idx]
                print(f'지원번호:{idx:02d}', end=' ')
                print(f'이름:{row["이름"]}', end=' ')
                for col in cols:
                    print(f'{col}:{row[col]:.0f}', end=' ')
                print()
                print('-' * 60)
            input('아무키나 누르세요!')
        elif menu=='3':
            input('아무키나 누르세요!')
        elif menu=='4':#삭제
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록된 지원번호가 아닙니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row = df.loc[no]
                print(f'이름:{row["이름"]}')
                for col in cols:
                    print(f'{col}:{row[col]}')
                sel=input('정말로 삭제하실래요(Y)>')
                if sel=='Y' or sel=='y':
                    score.drop(index=no, inplace=True)
                    score.to_csv(file_score)
                    print('삭제완료!')
            input('아무키나 누르세요!')
        elif menu=='5': #수정
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록된 지원번호가 아닙니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row = score.loc[no]
                print(f'이름>{info.loc[no, "이름"]}')
                grade=[]
                for col in cols:
                    num = inputNum(f'{col}:{row[col]}>')
                    if num=='':num = row[col]
                    grade.append(num)
                sel = input('정말로 수정하실래요(Y)>')
                if sel=='Y' or sel=='y':
                    score.loc[no] = grade
                    score.to_csv(file_score)
                    print('수정완료!')
                    
            input('아무키나 누르세요!')
        else:
            input('0~5번 숫자를 입력하세요!')

if __name__=='__main__':
    submenu()