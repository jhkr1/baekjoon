import sys

n = int(sys.stdin.readline())
words_list = []
for i in range(n):
    words_list.append(sys.stdin.readline().strip())

words_list = set(words_list)
words_list = list(words_list)
words_list.sort() # a,b,c 사전 순으로 정리 후
words_list.sort(key=lambda x:len(x)) # 다시 길이를 기준으로 정렬

for i in words_list:
    print(i)