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

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cur.execute(sql)
        row = cur.fetchone()
        return row['new_id']
    except Exception as err:
        print('새로운학번:', err)

def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']
            list.append(dept)
        return list
    except Exception as err:
        print('학과목록:', err)

if __name__=='__main__':
    depts = listDept()
    for dept in depts:
        print(f'{dept.dcode}.{dept.dname}', end='|')
    print()
    print('-' * 50)
    #while True:
        