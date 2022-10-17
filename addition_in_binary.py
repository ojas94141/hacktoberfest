def binadd(a,b):
    s=""
    while (a!=0 and b!=0):
        e=0
        c=a%10
        d=b%10
        x=c+d+e
        if x==0:
            s+="0"
        elif x==1:
            s+="1"
            if c!=0:
                c=0
        elif x==2:
            s+='1'
            c=1
        elif x==3:
            s+='1'
        a=a//10
        b=b//10
    if c!=0:
        s+=str(c)
    if a!=0:
        s+=str(a)[::-1]
    else:
        s+=str(b)[::-1]
    s=(s[::-1])
    return s

c=binadd(int(input()),int(input()))
print(c)
        
    
