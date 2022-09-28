try:
    import math
    n=int(input("N--->"))
    if(n<=0):
        print("INVALID VALUE")
    else:
        count=0
        for i in range(1,n+1):
            if(n%i==0):
                count+=1
        print("FACTORIAL--> ",math.factorial(n))
        print("TOTAL NUMBER OF FACTORS----> ",count)
except(ValueError):
    print("ALPHABETS ARE NOT ALLOWED")
