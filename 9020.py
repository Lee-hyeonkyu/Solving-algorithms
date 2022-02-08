m_n = 10000
c_l = [True for i in range(m_n)]

for i in range(2,int(m_n**0.5)):
    if c_l[i] == True:
        j = 2
        while i*j < m_n:
            c_l[i*j] = False
            j += 1
def p_n(number):
    if c_l[number] != True:
        return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    a = int(n/2)
    b = n-a
    while True:
        if p_n(a)==True & p_n(b)==True:
            print(b,a)
            break
        else:
            a+=1
            b=n-a