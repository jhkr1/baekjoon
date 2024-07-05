a, b, c, d, e = map(int, input().split())

p_list = [a, b, c, d, e]
sum = 0


for i in range(len(p_list)):
    p_list[i] = p_list[i] ** 2
    sum += p_list[i]

result = sum % 10

print(result)

