def returnSub(s):
    if len(s)==0:
        return ['']
    sa=returnSub(s[1:])
    z=[i for i in sa]
    for i in sa:
        z.append(s[0]+i)
    return z

s=input('Enter string: ')
print(returnSub(s))
