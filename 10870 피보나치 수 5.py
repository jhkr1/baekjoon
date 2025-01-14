def Fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return Fibonacci_number(n-1) + Fibonacci_number(n-2)


n = int(input())
result = Fibonacci_number(n)
print(result)

