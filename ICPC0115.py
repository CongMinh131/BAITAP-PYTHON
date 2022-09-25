def luythua(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
def kt(n):
    s=0
    while(n>0):
        a=n%10
        n=int(n/10)
        s=s+luythua(a)
    return s

t=int(input())
while t>0:
    n=int(input())
    if kt(n)==n:
        print("Yes")
    else:
        print("No")
    t=t-1