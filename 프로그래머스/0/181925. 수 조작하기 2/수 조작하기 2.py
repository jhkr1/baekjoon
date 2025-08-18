def solution(numLog):
    answer = ""
    key = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    return ''.join(key[b - a] for a, b in zip(numLog, numLog[1:]))