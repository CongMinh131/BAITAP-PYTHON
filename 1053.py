def tong(s):
    res=0
    for i in range(0,len(s)):
        res=res+int(s[i])
    return res
t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    if tong(s)%3==0:
        print("YES")
    else:
        print("NO")