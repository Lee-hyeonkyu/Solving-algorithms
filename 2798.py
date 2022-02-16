n,m = map(int,input().split())
c= list(map(int,input().split()))
sum_card= 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            three_card=c[i]+c[j]+c[k]
            if three_card<=m:
                sum_card= max(sum_card,three_card)
print(sum_card)