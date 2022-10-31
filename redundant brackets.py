#redundant brackets
a=input()
s=[]
count=0
bool=False
for i in range(len(a)):
    
    if a[i]=='(' and a[i+1]!='(':
        while a[i]!=')':
            if a[i]=='(' and a[i+2]==')':
                bool=True
                print(True)
                break
            s.append(a[i])
            i+=1
    if bool==True:
        break
    
    z=None
    if len(s)!=0:
        while z!='(':
            count+=1
            z=s.pop()
    if count <=1:
        print(True)
        break
        
if count>1 and bool==False:
    print(False)
