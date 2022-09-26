try:
    n=int(input("N---> "))
    if(n<=0):
        print("ZERO AND NEGATIVE IS NOT ALLOWDED")
        exit()
    else:
        count=0
        a=1
        while(count<n):
            sum=0
            for i in range(1,(a//2)+1):
                if(a%i==0):
                    sum=sum+i
            if(sum==a):
                print(a,end=" ")
                count+=1
            a+=1
except ValueError:
    print("FLOAT VALUES ARE NOT ALLOWDED")

