import sys
from collections import Counter
n = int(sys.stdin.readline())
num_list = []
if n % 2 == 1:
    for i in range(n):
        num_list.append(int(sys.stdin.readline()))

def mean(num_list):
    mean = 0
    for i in num_list:
        mean += i
    mean = (mean / len(num_list))
    return mean

def median(num_list):
    sort_num_list = sorted(num_list)
    median = sort_num_list[int(len(sort_num_list) / 2)]
    return median

def range(num_list):
    range = max(num_list) - min(num_list)
    return range


def mode(num_list):
    freq = Counter(num_list)
    most_common = freq.most_common()
    max_freq = most_common[0][1]

    mode_candidates = [num for num, cnt in most_common if cnt == max_freq]
    mode_candidates.sort()

    return mode_candidates[0] if len(mode_candidates) == 1 else mode_candidates[1]


print(round(mean(num_list)))
print(median(num_list))
print(mode(num_list))
print(range(num_list))



