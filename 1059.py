def kt(s):
    res=0
    for i in range(0,len(s)):
        if(i%2==1):
            res=res+int(s[i])
    if(res==0):
        return 1
    return 0
t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    res=1
    cnt=0
    for i in range(0,len(s)):
        if(i%2==1 and s[i]!="0"):
            res=res*int(s[i])
        elif(i%2==0):
            cnt=cnt+int(s[i])
    if(kt(s)==1):
        res=0
    print(cnt,res)
    