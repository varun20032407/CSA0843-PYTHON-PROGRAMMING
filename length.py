def sa(a,b):
    x=a.replace(' ','')
    y=b.replace(' ','')
    if(len(x)<len(b)):
        lth=len(x)
    else:
        lth=len(y)
    count=0
    for i in range(lth):
        if(x[i]!=y[i]):
            count=count+1
    print(lth-count)
a=input("ENTER THE STRING 1---> ")
b=input("ENTER THE STRING 2---> ")
sa(a,b)
