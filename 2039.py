def tong1(k,s):
    res=0
    for i in range(k,len(s)):
        res=res+int(s[i])
    return res
def tong2(l,s):
    res=0
    for i in range(0,l):
        res=res+int(s[i])
    return res
t=int(input())
k=1;l=0;cnt1=0;cnt2=0
while(t>0):
    s=input().split()
    if(k<len(s)):
        cnt1=cnt1+int(tong1(k,s))
    if(l>0):
        cnt2=cnt2+int(tong2(l,s))
    l=l+1
    k=k+1
    t=t-1
k=int(input())
if(cnt1-cnt2<=k):
    print("YES")
    print(abs(cnt1-cnt2))
else:
    print("NO")
    print(abs(cnt1-cnt2))

