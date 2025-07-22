import sys
n, m = map(int, sys.stdin.readline().split())

not_listen_people = set(sys.stdin.readline().strip() for _ in range(n))
not_see_people = set(sys.stdin.readline().strip() for _ in range(m))

intersection = sorted(not_listen_people & not_see_people)
print(len(intersection))
print('\n'.join(intersection))

# 리스트에서 집합으로 변경 -> 반복문을 사용하지 않으므로, 시간 단축
