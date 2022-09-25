n=int(input())
s=input().split()
t=0
for i in range(0,len(s)-1,2):
    if(s[i]!=s[i+1]):
        t=t+1
print(t)