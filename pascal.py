from math import factorial
n=int(input("ENTER THE NUMBER OF ROWS---> "))
if(n<=0):
    print("INAVLID")
    exit()
r=int(input("ENTER THE ROW NUMBER---> "))
if(r<=0):
    print("INVALID VALUES")
    exit()
else:
    summ=0
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
        print()
    for n in range(r-1):
        summ=summ+(1<<n)
    print("THE SUM OF",r,"ROW---> ",summ+1)
