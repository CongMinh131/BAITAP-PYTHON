def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def tong(s):
    res=0
    for i in range(0,len(s)):
        res=res+int(s[i])
    return res

def kt(s):
    for i in range(0,len(s)):
        a=int(s[i])
        if(i%2==0 and a%2!=0 ):
            return 0
        elif(i%2==1 and a%2==0):
            return 0
    return 1
t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    if nt(tong(s))==1 and kt(s)==1:
        print("YES")
    else:
        print("NO")
    