# 설탕공장에서 만드는 설탕 3kg or 5kg
# ex) 18kg -> 5kg 3개, 3kg 1개
# 배달하는 봉지의 최소 개수를 출력한다.
# 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# 6kg일때 문제가 발생 
# 몫을 비교해서 문제를 푼다면 18kg일때는 5로 나누었을 때 몫 3 3으로 나누었을 때 6


input = int(input())

a1, b1 = divmod(input, 5) # 5로 나눈 몫 a1, 나머지 b1
c1, d1 = divmod(b1, 3) # b1을 3으로 나눈 목 c1, 나머지 d1

print(a1, b1, c1, d1)

if(d1 > 0):
    result1 = -1
else:
    result1 = a1 + c1


a2, b2 = divmod(input, 3) # 5로 나눈 몫 a1, 나머지 b1
c2, d2 = divmod(b2, 5) # b1을 3으로 나눈 목 c1, 나머지 d1

print(a2, b2, c2, d2)

if (d2 > 0):
    result2 =  -1
else:
    result2 = a2 + c2


if(d1 > 0 and  d2 > 0):
    print(-1)
else:
    if(result1 == -1 or result2 == -1):
       print(max(result1, result2))
    elif(result1 != -1 and result2 != -1):
        print(min(result1, result2))




