import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.code})')
        print('-' * 50)    

def list():
    sql = 'select * from vstudent'
    cur.execute(sql)
    rows = cur.fetchall()
    list = []
    for row in rows:
        stu = Student()
        stu.id = row['id']
        stu.name = row['name']
        stu.dname = row['dname']
        stu.code = row['code']
        list.append(stu)
    return list

if __name__=='__main__':
    list = list()
    for stu in list:
        stu.print()