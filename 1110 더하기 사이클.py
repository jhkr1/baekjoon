def sum_cycle(n):
    a = n // 10
    b = n % 10
    t = a + b
    x = (b * 10) + (t % 10)
    return x


n = int(input())
original = n
cycle = 0

while(1):
    n = sum_cycle(n)
    cycle += 1

    if n == original:
        print(cycle)
        break

# def sum_cycle(n):
#     a, b = divmod(n, 10)
#     return (b*10) + ((a+b) % 10)
#
# n = int(input())
# original = n
# cycle = 0
#
# while True:
#     n = sum_cycle(n)
#     cycle += 1
#     if n == original:
#         break
# print(cycle)