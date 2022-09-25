t=int(input())
while(t>0):
    t=t-1
    s=input().split()
    l=input().split()
    x=a[0:int(s[1])]
    y=a[int(s[1]):]
    a=y+x
    a=' '.join(a)
    print(a)


