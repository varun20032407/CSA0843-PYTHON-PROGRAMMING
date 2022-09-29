n=int(input("ENTER THE NUMBER OF ELMENTS---> "))
arr=[]
for i in range(0,n):
    a=input("ENTER THE STRING---> ")
    arr.append(a)
print(arr)
ch=input("ENTER THE ORDER REQUIRED(ASCENDING-A/DESCENDING-D)---> ")
if(ch=='A' or ch=='a'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("THE ASCENDING ORDER")
    for i in range(0,n):
        print(arr[i])
elif(ch=='D' or ch=='d'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("THE DESCENDING ORDER")
    for i in range(0,n):
        print(arr[i])

