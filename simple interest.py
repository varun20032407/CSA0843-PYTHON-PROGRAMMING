p=float(input("ENTER THE PRINCIPLE AMOUNT---> "))
if(p<=0):
    print("INVALID ENTRY")
    exit()
yr=int(input("ENTER NUMBER OF YEARS---> "))
if(yr<=0):
    print("INVALID ENTRY GIVEN")
    exit()
ch=input("IS CUSTOMER SENIOR CITIZEN OR NOT(Y--YES/N--NO)---> ")
if(ch=='y' or ch== 'Y'):
    sii=(p*yr*12)/100
    print("INTEREST---> ",sii)
elif(ch=='n' or ch=='N'):
    si=(p*yr*10)/100
    print("INTEREST---> ",si)
else:
    print("INVALID")
