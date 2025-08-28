import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    port=3306,
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

def list(key):
    try:
        keys=['id', 'name', 'dname']
        sql = f'select * from vstudent order by {keys[key-1]}'         
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
    except Exception as err:
        print('학생목록오류:', err)

def search(value):
    try:
        sql = 'select * from vstudent where id like %s or name like %s or dname like %s'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value))
        rows = cur.fetchall()
        if not rows==None:
            list = []
            for row in rows:
                stu = Student()
                stu.id = row['id']
                stu.name = row['name']
                stu.code = row['code']
                stu.dname = row['dname']
                list.append(stu)
            return list
    except Exception as err:
        print('학생검색오류:', err)


if __name__=='__main__':
    while True:
        value = input('검색어>')
        if value=='': break
        students = search(value)
        if len(students)==0:
            print('검색학생이 없습니다.')
        else:
            for stu in students:
                stu.print()