try:
    sal=float(input("ENTER THE SALARY---> "))
    if(sal<=0):
        print("BYEEE")
        exit()
    ch=input("ENTER THE GRADE---> ")
    print("SALARY--- > ",sal)
    if(ch=='A' or ch=='a'):
        bon=sal*5/100
        tot=bon+sal
        print("BONUS---> ",bon)
        print("TOTAL SALARY---> ",tot)
    elif(ch=='B' or ch=='b'):
        bon=sal*10/100
        tot=bon+sal
        print("BONUS---> ",bon)
        print("TOTAL SALARY---> ",tot)
    else:
        print("INVALID")
        exit()
    if(sal<10000):
        if(ch=='A' or ch=='a'):
            bon=sal*7/100
            tot=bon+sal
            print("BONUS---> ",bon)
            print("TOTAL SALARY---> ",tot)
        elif(ch=='B' or ch=='b'):
            bon=sal*12/100
            tot=bon+sal
            print("BONUS---> ",bon)
            print("TOTAL SALARY---> ",tot)
        else:
            print("INVALID ENTRY")
            exit()
except(ValueError):
    print("ERROR")
    exit()
        
