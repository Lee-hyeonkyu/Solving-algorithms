def po_star(n):
    global a

    if n == 3:
        a[0][:3] = a[2][:3] = [1]*3
        a[1][:3] = [1,0,1]
        return

    u = n//3
    po_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(u):
                a[u*i+k][u*j:u*(j+1)] = a[k][:u]

x = int(input())

a = [[0 for i in range(x)] for i in range(x)]

po_star(x)

for i in a:
    for j in i:
        if j:
            print("*", end="")
        else:
            print(" ", end="")
    print()