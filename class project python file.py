import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="root",database="classproject")

def monitor():
    print("select 2 options: 1. update 2.check")
    i=int(input("enter the option"))
    if i==1:
        x=input("enter the roll: ")
        y=input("enter the name: ")
        z=input("enter the month: ")
        data=(x,y,z)
        sql='INSERT INTO monitor values(%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("data entered successfully")
        main()
    elif i==2:
        sql='SELECT * FROM monitor'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
        main()
def marks():
    print("select 2 options: 1. update 2.check")
    i=int(input("enter the option"))
    if i==1:
        x=input("enter the roll: ")
        y=input("enter the name: ")
        z=int(input("enter marks for s1: "))
        m=int(input("enter marks for s2: "))
        n=int(input("enter marks for s3: "))
        o= z+m+n
        p=(o/300)*100
        q=input("enter the month: ")
        data=(x,y,z,m,n,o,p,q)
        sql='INSERT INTO marks values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("data entered successfully")
        main()
    elif i==2:
        sql='SELECT * FROM marks'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
        main()

def attendance():
    print("select 2 options: 1. update 2.check")
    i=int(input("enter the option"))
    if i==1:
        x=input("enter the date in yyyy-mm-dd format: ")
        y=input("enter the absentece: ")
        data=(x,y)
        sql='INSERT INTO attendance values(%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("data entered successfully")
        main()
    elif i==2:
        sql='SELECT * FROM attendance'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
        main()
def students():
    print("select 2 options: 1. update 2.check")
    i=int(input("enter the option"))
    if i==1:
        x=input("enter the roll: ")
        y=input("enter the name: ")
        z=input("enter the phone: ")
        m=input("enter the address: ")
        data=(x,y,z,m)
        sql='INSERT INTO students values(%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("data entered successfully")
        main()
    elif i==2:
        sql='SELECT * FROM students'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
        main()
def main():
    print("choose from the following: 1. monitor 2.marks 3.attendance 4.students")
    i=int(input())
    if i==1:
        monitor()
    elif i==2:
        marks()
    elif i==3:
        attendance()
    elif i==4:
        students()
    else:
        print("enter from the following")
main()
        
