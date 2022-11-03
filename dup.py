a=int(input("ENTER THE NUMBER OF ELEMENTS---> "))
arr=[]
for i in range(0,a):
    n=input("Enter the elements---> ")
    arr.append(n)
d={x for x in arr if arr.count(x)>1}
print(d)
