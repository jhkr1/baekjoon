def solution(arr, k):
    if k % 2 != 0:   # 홀수
        return [x * k for x in arr]
    else:            # 짝수
        return [x + k for x in arr]