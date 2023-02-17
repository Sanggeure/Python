num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break

#1부터 +1해가면서 표시, 단, 10초과가 되면 차단시켜
# break = 즉시 반복 종료. break은 가장 가까운 while만 차단시킴
# 그리고 만약 break을 밖으로 빼면 while에 대해 break으로 작용, 반복하지 않고 1번만에 끝남

num = 1
while num <= 10:
    num += 1
    if num % 2 == 1:
        continue
    print(num)
# if 문은 참일 때만 실행
# 10이하의 짝수만 출력

num=2
while num<=10:
    print(num)
    num+=2

#10이하의 짝수만 출력 2방안