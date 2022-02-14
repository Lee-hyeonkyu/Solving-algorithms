x=str()
def bina(num):
    global x 
    if num<=1:
        x+=str(num)
        print(x[::-1])
        return
    x+=str(num%2)
    bina(num//2)
bina(int(input()))