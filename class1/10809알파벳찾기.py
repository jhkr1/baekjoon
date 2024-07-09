alphabet = [-1] * 26  # 알파벳 'a'부터 'z'까지의 처음 등장 위치를 저장할 리스트 초기화

word = input()  # 사용자로부터 입력 문자열을 받음

for i in range(len(word)):
    # 문자열을 한 글자씩 순회하면서
    # 현재 문자의 알파벳 인덱스 계산
    pos = ord(word[i]) - ord('a')
    
    # 만약 alphabet 리스트의 pos 인덱스에 저장된 값이 -1이라면
    if alphabet[pos] == -1:
        # 해당 알파벳이 처음 등장한 위치를 저장
        alphabet[pos] = i

# 결과 출력
for i in alphabet:
    print(i, end=' ')  # 각 알파벳의 처음 등장 위치 출력 (없으면 -1 출력)