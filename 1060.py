t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    res=1
    cnt=0
    for i in range(0,len(s)):
        if(i%2==0 and s[i]!="0"):
            res=res*int(s[i])
        else:
            cnt=cnt+int(s[i])
    print(res,cnt)