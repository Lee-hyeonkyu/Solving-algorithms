a,b = map(int,input().split())
c = int(input())
s_h = a
s_m = b+c
if s_m >= 60:
    s_h += s_m//60
    s_m %= 60
    if s_h >=24:
        s_h -=24
print(s_h,s_m)
