import os
path = os.path.dirname(os.path.realpath(__file__))
#print('현재패스', path)
file_name = path + '\product.txt'
#print('파일명', file_name)

class Product:
    def __init__(self):
        self.code=0
        self.name=''
        self.price=0
    def print(self):
        print(f'코드:{self.code},상품명:{self.name},가격:{self.price:,}만원')

#데이터 하나 추가 함수
def fileAppend(p):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{p.code},{p.name},{p.price}\n')

def append():
    p = Product()
    p.code = 2
    p.name = '세탁기'
    p.price = 500
    fileAppend(p)
    print('등록성공!')

append()