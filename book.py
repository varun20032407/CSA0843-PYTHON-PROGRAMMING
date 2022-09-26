n=int(input("NUMBER OF COPIES REQUIRED---> "))
pb=250
dpb=0.2*pb
if(n<=0):
    print("INVALID")
    exit()
elif(n<=5):
    sc=20
    tot=dpb+sc
    print("DISCOUNT PRICE---> ",dpb)
    print("TOTAL PRICE---> ",tot)
else:
    d=5*20
    scc=55*25
    tot=d+scc+dpb
    print("DISCOUNT PRICE---> ",dpb)
    print("TOTAL PRICE---> ",tot)
