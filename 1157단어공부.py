word = input().strip().upper()
frequency = [0] * 26 # 알파벳 빈도를 저장할 리스트
for char in word:
    index = ord(char) - ord('A')
    frequency[index] += 1

max_f = max(frequency)

result = [i for i in range(26) if frequency[i] == max_f]

if len(result) > 1:
    print('?')
else:
    print(chr(result[0] + ord('A')))