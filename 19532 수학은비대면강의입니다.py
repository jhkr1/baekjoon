# import sys
# from sympy import symbols, solve
#
# try:
#     a, b, c, d, e, f = map(int, sys.stdin.readline().split())
# except:
#     print(f'{e}')
#
#
# x, y = symbols('x y')
#
# equation1 = (a*x) + (b*y) -c
# equation2 = (d*x) + (e*y) - f
#
# result = solve((equation1, equation2), (x, y))
# if isinstance(result, dict):
#     print(result[x], result[y])

import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            break


