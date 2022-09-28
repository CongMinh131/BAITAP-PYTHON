def fibo(n):
    if(n<0):
        return -1
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
t=int(input())
while(t>0):
    s=input().split()
    a=int(s[0])
    b=int(s[len(s)-1])
    for i in range(a,b+1):
        print(fibo(i),end=" ")
