t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split()
    lis=[]
    for i in range(0,len(s)):
        lis.append(s[i])
    res=0;m=3
    while(m>0):
        res=res+int(min(lis))
        lis.remove(min(lis))
        m=m-1
    print(res)