import math
t= int(input())
for i in range(t):
    x,y,r,x1,y1,r1 = map(int,input().split())
    a=math.sqrt(((x-x1)**2+(y-y1)**2))
    b=r+r1
    c=abs(r-r1)
    if a==0:
        if r==r1:
            print(-1)
        else:
            print(0)
    else:
        if a == b or a == c:
            print(1)
        elif a < b and a > c:
            print(2)
        else:
            print(0)