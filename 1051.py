def tong(s):
    res=0
    for i in range(0,len(s)):
        res=res+int(s[i])
    return res
        
def tn(n):
    s=str(n)
    s1=s[::-1]
    if(s==s1):
        return 1
    return 0

t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    if(tn(tong(s))==1):
        print("YES")
    else:
        print("NO")
