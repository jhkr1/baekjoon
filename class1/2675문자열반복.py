t = int(input())
result_list = []

for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)
    result = ''
    for char in s:
        result += char * r
    result_list.append(result)

    
for i in result_list:
    print(i)