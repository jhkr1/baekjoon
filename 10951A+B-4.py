import sys
sum_list = []

for i in sys.stdin:
    # 줄이 공백일 경우 반복문 종료
    if i.strip() == "":
        break

    a, b = map(int, i.split())
    sum_list.append(a+b)

for result in sum_list:
    print(result)


