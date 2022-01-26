"""import psycopg2

try:
    connection_1 = psycopg2.connect(host='127.0.0.1',
                                    user='maktab_user',
                                    password='123456', dbname='Photography')
    curs = connection_1.cursor()
    curs.execute("select * from camera")
    result = curs.fetchall()
except Exception as e:
    print(e)"""
# curs.execute("select * from departments")
# result = curs.fetchall()
# create_table_query = """create table emp_log
# (emp_no int primary key not null,
# log_date date not null,
# start_work time not null,
# end_work time not null);"""
# curs.execute(create_table_query)
# curs.execute("select * from emp_log")
# result = curs.fetchall()

# connection_1.commit(
import psycopg2
connection = psycopg2.connect(host='localhost', user='postgres', password='S87', dbname='ITRA')
cur = connection.cursor()
# cur.execute("""INSERT INTO runner(first_name,last_name,birth_date,gender)
# Values
# ('Ali','Ahmadi','1998-04-10','M'),
# ('Adele','Beigi','1997-12-08','F')
# """)
runner_info = ['Meimanat','Jalilian','1990-05-25','F']
str = 'INSERT INTO runner(first_name,last_name,birth_date,gender)Values (%s,%s,%s,%s) '
cur.execute(str,runner_info)
connection.commit()
def display(name):
    cur.execute("""SELECT *
                        FROM runner
                        WHERE first_name=%s
                            """,(name,))
    print(cur.fetchall())
display('Ali')
