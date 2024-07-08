import sys
sum_list = []

for i in sys.stdin:
    if i.strip() == "":
        break

    a, b = map(int, i.split())
    sum_list.append(a+b)

for result in sum_list:
    print(result)


