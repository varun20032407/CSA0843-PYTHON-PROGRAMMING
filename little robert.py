n=int(input("ENTER THE NUMBER OF ELEMENTS----> "))
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
print(arr)
count=0
for j in range(1,arr[i]+1):
    if(arr[i]%j==0):
        count+=1
print("FACTORS---> ",count-2)
