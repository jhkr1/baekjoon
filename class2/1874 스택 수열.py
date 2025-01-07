n = int(input())  # 수열의 길이
sequence = [int(input()) for _ in range(n)]  # 목표 수열 입력

stack = []  # 스택
result = []  # 연산 기록
current = 1  # 현재 스택에 push할 숫자

possible = True  # 수열 생성 가능 여부

for num in sequence:
    while current <= num:  # 목표 숫자에 도달할 때까지 push
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == num:  # 스택의 top이 목표 숫자와 같으면 pop
        stack.pop()
        result.append("-")

    else:  # 목표 숫자를 만들 수 없는 경우
        possible = False
        break

if possible:
    print("\n".join(result))  # 연산 출력
else:
    print("NO")