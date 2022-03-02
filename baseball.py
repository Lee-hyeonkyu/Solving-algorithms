import random

print("맞출 숫자의 갯수를 입력해주세요.*권장:3* ")
the_number_of_ball = int(input())
print("선택하신 갯수는"+ str(the_number_of_ball) +"입니다.")
baseball = "".join(map(str,random.sample(range(1,10),the_number_of_ball)))
print(baseball)
count = 0
while 1:
    strike = 0
    ball = 0
    count +=1
    print("숫자를 입력해주세요")
    my_ball = input()
    if(my_ball==baseball):
        break
    for i in range(the_number_of_ball):
        if(baseball[i]==my_ball[i]):
                strike += 1
        else:
            for j in range(the_number_of_ball):
                if(baseball[i]==my_ball[j]):
                    ball += 1
    print("{0}스트라이크 {1}볼 입니다.{2}회 입니다.".format(strike,ball,count))
print("정답입니다. 총 {0}번 만에 맞췄습니다.".format(count))