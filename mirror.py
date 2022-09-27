try:
    n=int(input("ENTER THE NUMBER---> "))
    rev=0
    if(n<0):
        print("NEGATIVE VALUE")
        exit()
    else:
        while(n!=0):
            d=n%10
            rev=(rev*10)+d
            n//=10
        print("MIRRO IMAGE---> ",str(rev))
except ValueError:
    print("ALPHABETS ARE NOT ALLOWDED") 
    
