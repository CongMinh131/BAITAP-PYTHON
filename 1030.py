
def gcd(a,b):
    while (b != 0) :
        c = a % b
        a = b
        b = c
    return a
def kt(s):
    if(s==10):
        print("\n")
    else:
        print(" ")

a,b=map(int,input().split())
n=10**(b-1)
m=10**b
s=0
for i in range(n,m):
    if(gcd(i,a)==1):
        s=s+1
        if(s==10):
            print(i,end=" ")
            print("\n")
            s=0
        else:
            print(i,end=" ")

