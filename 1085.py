x,y,w,h = map(int,input().split())

a=0 
b=0

if (x-0)<(w-x):
    a = x-0
else:
    a = w-x

if (y-0)<(h-y):
    b = y-0
else:
    b = h-y

if a<b:
    print(a)
else:
    print(b)