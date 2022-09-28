def ors(n):
    if(n<=0):
        print("NEGATIVE AND ZERO")
        exit()
    if(n<=1):
        return(n*750)
    elif(n>1):
        return(((n-1)*200)+750)
n=int(input("ENTER THE QUANTITY----> "))
print("SHIPPING CHARGES----> ","%.2f"%(ors(n)))

