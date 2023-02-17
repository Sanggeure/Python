for num in range(1, 11):
    print(num)

# 1~10 출력해달라는 코드
# 일반적으로 앞은 포함, 뒤는 미포함

for num in range(1, 11):
    if num % 2 == 1:
        print(num)
# 홀수만 출력하기

# 함수 안에 들어가는 것 ( 0 , 0 , 0 ) 함수 안에 들어간 0과같은 존재를 parameter, 인자, 매개변수 라고 부른다

for num in range(1, 11, 2):
    print(num)
# 홀수만 출력 - 원리: 3번째 parameter 뜻은 그만큼 점프한다는 것. +2가 된다. (마치 등차수열같다)
