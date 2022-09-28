n=int(input("ENTER THE NUMBER OF ELEMENTS---> "))
if(n<=0):
    print("INVALID ENTRY")
    exit()
arr=[]
for i in range(0,n):
    a=int(input("ENTER THE ELEMENTS---> "))
    arr.append(a)
en=0
od=0
count=0
for i in range(0,n):
    if(arr[i]%2==0):
        en=en+(arr[i]*arr[i])
    else:
        od=od+(arr[i]*arr[i])
print("SUM OF SQUARE OF EVEN NUMBERS---> ",en)
print("SUM OF SQUARE OF ODD NUMBERS---> ",on)
