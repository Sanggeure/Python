'''
for num in range (1,10):
    print ("2 " + str(num), 2*num)

for num in range(1, 10):
    print(2, num, 2 * num)
'''

# 구구단 만들기
for num1 in range(1, 10):
    for num2 in range(1, 10):
        print(num1, '*', num2, '=', num1 * num2)
        #콤마 뒤에는 반드시 공백이 들어가기 때문에 불필요 하다면 부적합할 수 있음
        # print(str(num1) + ' * ' + str(num2) + ' = ' + str(num1 * num2))
        # print('%d * %d = %d' % (num1, num2, num1 * num2))
        # %d = decimal 십진수의 약자. %d가 num1, num2를 따와서 들여온다.
        # 문자 포맷팅이라고 부르는 방식.
        # %s (문자받는), %b (2진수 받는), #o (8진수 받는)
        # 8진수, 16진수를 쓰는 일은 생각보다 많음.
'''
나는 과연 3*1 3*2 3*3의 숫자 순서로 나올지 우려했지만, 1~9까지 순서대로 나오는 게 규칙이기때문에 당연히 순차적으로 나옴
'''
