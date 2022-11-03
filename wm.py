import datetime
import numpy
m=input("enter the month:- ")
y=int(input("enter the year:- "))
m1=input("enter the month and year:- ")
if(y%4==0)and(y%400==0)and(y%100!=0)and(m=="February")or(m=="february"):
    d=29-4
    print("Number of working days:- ",d)
elif(m=="february")or(m=="February"):
    d=28-4
    print("Number of working days:- ",d)
elif(m=="January")or(m=="january")or(m=="may")or(m=="May")or(m=="July")or(m=="july")or(m=="october")or(m=="October"):
    d=31-5
    print("Number of working days:- ",d)
elif(m=="March")or(m=="march")or(m=="August")or(m=="august")or(m=="December")or(m=="december"):
    d=31-4
    print("Number of working days:- ",d)
elif(m=="April")or(m=="april")or(m=="June")or(m=="june")or(m=="September")or(m=="september")or(m=="november")or(m=="November"):
    d=30-4
    print("Number of working days:- ",d)
dd=numpy.busday_offset(m1,0,roll='forward',weekmask='Mon')
print(dd)
