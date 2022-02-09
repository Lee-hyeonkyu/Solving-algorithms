while True:
    a,b,c=map(int,input().split())
    if a==0 & b==0 & c==0:
        break
    a**=2
    b**=2
    c**=2
    if(max(a,b,c)*2-(a+b+c))==0:
        print("right")
    else:
        print("wrong")