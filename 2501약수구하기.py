n, k = map(int, input().split())
n_list = []
# n의 약수 찾기(a보다 작은 수 중에서)
for i in range(n):
    if (n % (i+1) == 0):
        n_list.append((i+1))
    else:
        continue

if (k-1 >= len(n_list)):
    print(0)
else:
    print(n_list[k-1])
