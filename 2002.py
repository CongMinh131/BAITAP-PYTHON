def fibo(n):
    f1 = 1
    f2 = 1
    fn = 2
    if (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f1 = f2
            f2 = fn
            fn = f1 + f2
        return fn
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        print(fibo(i),end=" ")