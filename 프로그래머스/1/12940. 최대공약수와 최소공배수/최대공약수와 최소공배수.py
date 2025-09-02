def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(n, m):
    return n * m // gcd(n, m)

def solution(n, m):
    if n > m:
        answer1 = gcd(n, m)
    else:
        answer1 = gcd(m, n)

    return answer1, lcm(n, m)
    

    
        