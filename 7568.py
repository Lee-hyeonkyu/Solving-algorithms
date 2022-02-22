n = int(input())
li= []
for i in range(n):
    w,h = map(int,input().split())
    li.append((w,h))

for i in li:
    x=1
    for j in li:
        if i[0] < j[0] and i[1]<j[1]:
            x +=1
    print(x, end=" ")