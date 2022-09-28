sr=int(input("ENTER THE STARTING RANGE---> "))
if(sr<=0):
    print("INVALID")
    exit()
er=int(input("ENTER THE ENDING RANGE---> "))
if(er<=0):
    print("INVALID ENTRY")
    exit()
k=int(input("ENTER THE NUMBER TO BE SKIPPED---> "))
if(k<=0):
    print("INVALID VALUE")
    exit()
print("THE NUMBERS ARE")
for i in range(sr,er,k+1):
    print(" ",i)
