a, b = map(int, input().split())
result1 = 0
result2 = 0
n = 2
while ((a > n) & (b > n)):
    result = 0
    if((a % n != 0) | (b % n != 0)):
        n += 1
        continue
    elif((a % n == 0) & (b % n ==0)):
        result = n
        continue
    result1 = max(result, n)

    

print(result1)

