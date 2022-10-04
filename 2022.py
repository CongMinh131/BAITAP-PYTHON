def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

n=int(input())
s=input().split()
l=[]
for i in range(0,len(s)):
    a=int(s[i])
    if(nt(a)):
        l.append(a)
d=dict.fromkeys(l)
l1=list(d)
for i in range(0,len(l1)):
    b=l.count(l1[i])
    print(l1[i],b)


