import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="root")
c=con.cursor()
sql1="drop database if exists classproject"
c.execute(sql1)

sql2="create database classproject"
c.execute(sql2)

sql3="USE classproject"
c.execute(sql3)
sql4="create table monitor(roll varchar(50),name varchar(50), month varchar(20))"
c.execute(sql4)
sql5="create table marks(roll varchar(50),name varchar(50),s1 int,s2 int,s3 int,total int,per float,term varchar(50))"
c.execute(sql5)

sql6="create table attendance(date date default current_date,abs varchar(100))"
c.execute(sql6)

sql7="create table students(roll varchar(50),name varchar(50),phone varchar(50),address varchar(50))"
c.execute(sql7)
con.commit()
