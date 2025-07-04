def solution(numbers):
    ret = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ret.append(numbers[i] + numbers[j])
    ret = sorted(set(ret))
    return ret

numbers = list(map(int, input().split()))
result = solution(numbers)
print(result)