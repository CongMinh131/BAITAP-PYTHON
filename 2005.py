n=int(input())
s=input().split()
t=0;
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        a=int(s[i])
        b=int(s[j])
        if a>b:
            t=t+1
print(t)
