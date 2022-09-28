try:
    def f(x):
        cnt=0
        print("\nTHE FACTORS OF",x,"ARE--->\n")
        for i in range(1,x+1):
            print(i)
            cnt=cnt+1
            if(cnt==m):
                break
    n=int(input("N--->"))
    if(n<=0):
        print("INVALID ENTRY")
        exit()
    m=int(input("M--->"))
    if(m<=0):
        print("INVALID")
        exit()
    else:
        count=0
        a=1
        clist=[]
        while(count<n):
            summ=0
            for i in range(1,(a//2)+1):
                if(a%i==0):
                    summ=summ+i
            if(summ==a):
                print(a,end=' ')
                clist.append(a)
                count+=1
            a+=1
        for i in clist:
            f(i)
except(ValueError):
    print("FLOAT VALUE ENTRY")
    exit()
            
