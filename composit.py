sr=int(input("A----> "))
if(sr<=0):
    print("INVALID")
    exit()
er=int(input("B----> "))
if(er<=0):
    print("INVALID")
    exit()
if(sr==er):
    print("BOTH CAN'T BE SAME VALUE")
    exit()
elif(sr>er):
    print("LARGE VALUE")
    exit()
else:
    f=0
    for i in range(sr+1,er):
        f=0
        for j in range(1,i):
            if(i%j==0):
                f+=1
        if(f>1):
            print(i)
