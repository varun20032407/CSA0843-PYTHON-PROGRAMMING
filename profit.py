def pro(price,n):
    profit=[0]*n
    mp=price[n-1]
    for i in range(n-2,0,-1):
        if(price[i]>mp):
            mp=price[i]
        profit[i]=max(profit[i+1],mp-price[i])
    mip=price[0]
    for i in range(1,n):
        if(price[i]<mip):
            mip=price[i]
        profit[i]=max(profit[i-1],profit[i]+(price[i]-mip))
    res=profit[n-1]
    return res
nn=int(input("ENTER NUMBER OF ELEMENTS---> "))
arr=[]
for i in range(0,nn):
    z=int(input("ENTER THE ELEMENT---> "))
    arr.append(z)
print("MAXIMUM PROFIT OBTAINED IS----> ",pro(arr,len(arr)))
