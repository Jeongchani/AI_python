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
        print(f'학번:{self.id}, 학과:{self.dname}({self.dept}), 이름:{self.name}')

def list():
    try:
        cur = con.cursor()
        sql = 'select s.*, d.name as dname from student as s, dept as d where s.dept=d.code'
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

if __name__=='__main__':
    students = list()
    if students!=None:
        for stu in students:
            stu.print()