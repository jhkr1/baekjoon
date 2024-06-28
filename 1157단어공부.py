word = input().strip().upper() # 대문자로 전부 입력을 받겠다.
frequency = [0] * 26 # 알파벳 빈도를 저장할 리스트
for char in word: # 단어길이만큼 반복
    index = ord(char) - ord('A') # 한 글자마다 아스키코드 숫자로 변환하여, 인덱스로 저장
    frequency[index] += 1 # 인덱스에 갯수 +1

max_f = max(frequency) # 가장 큰 값을 max_f에 저장

# result(리스트)에 i를 넣겠다. 리스트의 인덱스와 가장 큰 값이 같다면  
result = [i for i in range(26) if frequency[i] == max_f]

if len(result) > 1: # 만약 길이가 1보다 크다면 같은 빈도 수의 글자가 있는 것이므로 '?' 출력
    print('?')
else:
    print(chr(result[0] + ord('A')))
    # 아닐 경우 result(리스트)의 첫 번째 값(숫자) + 'A'의 아스키 코드를 더해서 원래 한 글자를 출력한다. 