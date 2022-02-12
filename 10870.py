fibo = [0]*3
for i in range(2,21):
    fibo[1]=1
    fibo[i]= fibo[i-1]+fibo[i-2]
    fibo.append(fibo[i])
print(fibo[int(input())])