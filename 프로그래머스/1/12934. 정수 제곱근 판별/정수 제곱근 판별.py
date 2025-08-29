import math

def solution(n):
    t = math.sqrt(n)
    if t.is_integer():
        return (t+1)**2
    else:
        return -1