# n = int(input()) # 상근이의 숫자 카드 개수
# num_cards = list(map(int, input().split()))
#
# m = int(input())
# compare_cards = list(map(int, input().split()))
#
# result = [0 for x in range(len(compare_cards))]
#
#
# for i in range(len(num_cards)):
#     for j in range(len(compare_cards)):
#         if compare_cards[j] == num_cards[i]:
#             result[j] += 1
#
# print(' '.join(map(str, result)))

import sys
from collections import Counter

n = int(sys.stdin.readline())
num_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare_cards = list(map(int, sys.stdin.readline().split()))

cards_count = Counter(num_cards)

print(cards_count)
result = [cards_count[card] for card in compare_cards]
print(' '.join(map(str, result)))

