def toh(n,a,b,c):
    if n==1:
        print(a,c)
        return
    toh(n-1,a,c,b)
    print(a,c)
    toh(n-1,b,a,c)

n=int(input())
print(2**n-1)
toh(n,1,2,3)