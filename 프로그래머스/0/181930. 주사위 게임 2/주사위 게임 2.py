def solution(a, b, c):
    if a != b and b != c and c != a:
        return a + b + c
    elif (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
        return (a + b + c) * (a*a + b*b + c*c)
    else:
        return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    