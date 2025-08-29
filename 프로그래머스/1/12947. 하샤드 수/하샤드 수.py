def solution(n):
    sum_num = sum(int(d) for d in str(n))
    return True if n % sum_num == 0 else False