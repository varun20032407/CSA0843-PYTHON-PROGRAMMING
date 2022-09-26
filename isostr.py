a=input("ENTER THE FIRST STIRNG---> ")
b=input("ENTER THE SECOND STRING---> ")
m=200
c=len(a)
d=len(b)
if(c!=d):
    print(False)
x=[False]*m
map=[-1]*m
for i in range(b):
    if(map[ord(a[i])]==-1):
        if(map[ord(b[i])])==True:
           print(False)
        x[ord(b[i])]=True
        map[ord(a[i])]=b[i]
    elif(map[ord(a[i])])!=b[i]:
        print(False)
print(True)
        

