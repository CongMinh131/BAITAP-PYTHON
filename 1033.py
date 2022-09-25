def gcd(a,b):
    while (b != 0) :
        c = a % b
        a = b
        b = c
    return a

a,b=map(int,input().split())
for i in range(a,b+1):
    for j in range(a,b+1):
        for k in range(a,b+1):
            if(gcd(i,k)==1 and gcd(i,j)==1 and gcd(j,k)==1):
                print("("+i+","+j+","+k)
