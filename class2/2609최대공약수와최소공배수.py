# ## 이 코드의 문제점 -> 런타임 에러 발생 
# a, b = map(int, input().split())

# temp = max(a, b)
# max_list = []

# for i in range(2, temp):
#     if ((a % i == 0) & (b % i == 0)):
#         max_list.append(i)

# result1 = max(max_list)

# result2 = (a * b) // result1
# print(result1)
# print(result2)

def gcd(a, b):
    while b: # b가 0이 아닌동안 반복
        a, b = b, a % b
    return a

def lcm(a, b, gcd_val):
    return (a * b) // gcd_val

a, b = map(int, input().split())
gcd_val = gcd(a, b)
lcm_val = lcm(a, b, gcd_val)

print(gcd_val)
print(lcm_val)

    