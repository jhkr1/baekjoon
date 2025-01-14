num_list = list(map(int, input().split()))

for idx in range(len(num_list)):
    if max(num_list) == num_list[idx]:
        num_list.pop(idx)
        break

print(max(num_list))


