# A, B, V
# 달팽이는 낮에 A미터 올라간다.
# 달팽이는 밤에 B미터 내려간다.
# V미터 올라가려면 어떻게 해야할까?
# a, b, v = map(int, input().split())
# day = 0
# height = 0

# while height < v:
#     day += 1
#     height += a
#     if height >= v:
#         break
#     height -= b

# print(day)

# 반복문을 사용했을 때 문제점 -> v의 숫자가 커질 수록 시간 복잡도가 너무 증가함.
a, b, v = map(int, input().split())
# 실제로 하루에 올라가는 높이이다.
oneday_height = a - b 
# 마지막 날에는 더이상 내려가지 않는다. -> 올라간 후 높이에 도달하면 종료
# 따라서 높이에서 내려가는 높이를 뺀 v - b에 대해 계산해야한다.

if (v - b) % oneday_height == 0:
    days = (v - b) // oneday_height
else:
    days = (v - b) // oneday_height + 1

print(days)


