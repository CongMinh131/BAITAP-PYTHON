def kt(s):
    s1=""
    l=len(s)
    cnt=1
    for i in range(0,l-1):
        if(s[i]==s[i+1]):
            cnt=cnt+1
        s1=str(cnt)+s[i]
    return s1

s=str(input())

