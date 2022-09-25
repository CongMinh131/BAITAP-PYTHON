def kt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def dk1(s):
    n=int(s)
    t=0
    while(n>0):
        t=t+n%10
        n=int(n/10)
    if(kt(t)):
        return 1
    return 0
def dk2(s):
    for i in range(0,len(s)):
        if(s[i]!='1' or s[i]!="" or s[i]!="3" or s[i]!="5" or s[i]!="7" ):
            return 0
    return 1
def dk3(s):
    s1=s[::-1]
    n=int(s1)
    if(kt(n)==1):
        return 1
    return 0
t=int(input())
while t>0:
    s=str(input())
    if(dk1(s)==1 and dk2(s)==0):
        print("Yes")
    else:
        print("No")
    t=t-1