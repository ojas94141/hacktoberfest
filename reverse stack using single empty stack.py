def reverseStack(a,b):
    if len(a)==1:
        return a
    n=len(a)
    for j in range(n-1):
        b.append(a.pop())
    z=a.pop()
    for k in range(n-1):
        a.append(b.pop())
    reverseStack(a,b)
    a.append(z)

a=[1,2,3,4,5]
b=[]
reverseStack(a,b)
print(a)
