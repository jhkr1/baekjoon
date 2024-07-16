# # 재귀함수 사용시 런타임 에러 발생.
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# n, k = map(int, input().split())
# result = factorial(n) // (factorial(n-k) * factorial(k))
# print(int(result))
    
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def combination(n, k):
    if (k > n):
        return 0
    return factorial(n) // (factorial(n-k) * factorial(k))

n, k = map(int, input().split())
result = combination(n, k)
print(result)


    