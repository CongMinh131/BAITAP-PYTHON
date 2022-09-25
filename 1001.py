def kt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1



n=int(input())
if(kt(n)):
    print("YES")
else:
    print("NO")
