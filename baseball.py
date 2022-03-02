import random

INPUT_ERROR =  "잘못 입력하였습니다. 다시 입력해주세요."

def start():
        global the_number_of_ball
        global baseball
        try:
            the_number_of_ball = int(input("맞출 숫자의 개수를 입력해주세요.*권장3*: "))
            baseball = "".join(map(str,random.sample(range(1,10),the_number_of_ball)))
            print(baseball)  # 정답
            if the_number_of_ball == 0:
                raise ValueError
        except ValueError:
            print(INPUT_ERROR + " 최대 9")
            start()
        
def main():
    try:
        count = 0
        while 1:
            strike = 0
            ball = 0
            count +=1
            my_ball = str(int(input("숫자를 입력해주세요: ")))
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
    except:
        print(INPUT_ERROR)
        main() 
start()
main()