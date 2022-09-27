try:
    n=int(input("ENTER THE NUMBER OF ELEMENTS----> "))
    arr=[]
    for i in range(0,n):
        a=int(input("ENTER THE ELEMENTS---> "))
        arr.append(a)
    if(arr[i]<0):
        print("NEGATIVE VALUES ARE NOT ALLOWEDED")
        exit()
    elif(arr[i]==16):
        print("SAME VALUE")
        exit()
    elif(arr[i]==0):
        print("SAME VALUE")
        exit()
    else:
        print(arr)
    print("ASCENDING ORDER")
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    for i in range(0,n):
        print(arr[i])
    x=int(input("ENTER THE VALUE OF N----> "))
    print("NTH MINIMUM NUMBER IS---> ",arr[x-1])
    diff=arr[x-1]
    print("DESECENDING ORDER")
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    for i in range(0,n):
        print(arr[i])
    y=int(input("ENTER THE VALUE OF M----> "))
    print("MTH MAXIMUM NUMBER IS--->  ",arr[y-1])
    summ=arr[y-1]
    print("SUM---> ",summ+diff)
    print("DIFFERNECE----> ",summ-diff)
except(IndexError):
    print("NTH OR MTH VALUE CAN'T BE GREATER")
