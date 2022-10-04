s=str(input())
s1=s[::-1]
l=len(s1)
t=0
ls=[]
for i in range(0,l):
    if(t==3):
        ls.append(",")
        t=0
    t=t+1
    ls.append(s1[i])
for i in range(len(ls)-1,-1,-1):
    print(ls[i],end="")
    
