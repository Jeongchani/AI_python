import os, sqlite3
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/haksa.db'

con = sqlite3.connect(db_name)

class Dept:
    def __init__(self):
        self.code=0
        self.dname=''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.dept=0

    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.dept})')

def list():
    try:
        cur = con.cursor()
        sql = 'select * from vstudent'
        cur.execute(sql)
        rows = cur.fetchall()
        list=[]
        for row in rows:
            stu = Student()
            stu.id = row[0]
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('목록 에러:', err)
    finally:
        pass

def search(value):
    try:
        cur = con.cursor()
        sql  ='1select * from vstudent where name like ? or id like ? or dname like ?'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value,))
        rows = cur.fetchall()
        list=[]
        for row in rows:
            stu = Student()
            stu.id = row[0]
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('검색오류:', err)
    finally:
        pass

def newID():
    try:
        cur = con.cursor()
        sql ='select max(id)+1 from student'
        cur.execute(sql)
        row = cur.fetchone()
        new_id = row[0]
        return new_id
    except Exception as err:
        print('코드생성:', err)
    finally:
        pass

def insert(stu):
    try:
        cur = con.cursor()
        sql = 'insert into student(id, name, dept) values(?,?,?)'
        cur.execute(sql, (stu.id, stu.name, stu.dept,))
        con.commit()
    except Exception as err:
        print('입력오류:', err)
    finally:
        pass

if __name__=='__main__':
    stu = Student()
    stu.id = newID()
    print(f'학번:{stu.id}')
    stu.name=input('이름>')
    if stu.name=='':
        print('이름을  반드시 입력하세요!')
    else:
        stu.dept = int(input('학과>'))
    insert(stu)