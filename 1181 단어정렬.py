# 소문자 알파벳에 반복문을 사용하여 가중치를 둔다.
# chr함수는 아스키코드를 문자로 바꾸는 함수.
weights = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z')+1)}
n = int(input())
words = [input() for _ in range(n)]

min_len = 51
min_idx = -1


