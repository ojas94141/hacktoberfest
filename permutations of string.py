def permutation(s):
    if len(s)==0:
        return ['']
    ans=[]
    for i in range(len(s)):
        z=s[i]
        new=s[:i]+s[i+1:]
        y=permutation(new)
        for i in y:
            ans.append(z+i)
    return ans

s=input('Enter String: ')
print(permutation(s))
