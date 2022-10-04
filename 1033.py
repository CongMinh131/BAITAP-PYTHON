def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

s=input().split()
a=int(s[0])
b=int(s[len(s)-1])
for i in range(a,b-1):
    for j in range(i+1,b):
        for k in range(j+1,b+1):
            if gcd(i,j)==gcd(j,k)==gcd(i,k)==1:
                print((i,j,k))