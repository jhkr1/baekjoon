import itertools

def solution(number):
    answer = 0
    combination_list = list(map(list, itertools.combinations(number, 3)))

    for i in combination_list:
        if sum(i) == 0:
            answer += 1

    return answer