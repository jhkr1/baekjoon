n = int(input())
result = []
for i in range(n):
    str_case = input()
    result.append(str_case[0]+str_case[-1])

for i in range(len(result)):
    print(result[i])
