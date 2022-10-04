def tc(a):
    res=1
    while(a>0):
        res=res*int(a%10)
        a=int(a/10)
    return res

t=int(input())
while(t>0):
    t=t-1
    n=input().split()
    s=input().split()
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            a=int(s[i])
            b=int(s[j])
            if tc(a)>tc(b):
                s[i],s[j]=s[j],s[i]
            elif tc(a)==tc(b) and a>b:
                s[i],s[j]=s[j],s[i]     
    for i in range(0,len(s)):
        print(s[i],end=" ")
    print()