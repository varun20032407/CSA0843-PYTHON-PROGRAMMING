def im(a,b):
    if len(a)!=len(b):
        return False
    else:
        m1,m2={},{}
        for i in range(len(a)):
            c,ch=a[i],b[i]
            if(c not in m1):
                m1[c]=ch
            if(ch not in m2):
                m2[ch]=c
            if(m1[c]!=ch)or(m2[ch]!=c):
                return False
    return True
a=input("S--> ")
b=input("T--> ")
print(im(a,b))
