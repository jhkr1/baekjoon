cols, rows = 100, 100
paper = [[0] * cols for _ in range(rows)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split()) # (x, y)를 입력 받아 그 점을 기점으로 가로 10, 세로 10의 정사각형을 그린다.
    if (x > 90 or y > 90):
        break
    for k in range(10):
        for j in range(10):
            paper[x+k][y+j] += 1


# 겹치는 부분을 제외한 넓이를 구함
total_area = 0
for row in paper:
    for value in row:
        if value > 0:  # cell이 0보다 큰 경우에만 넓이를 더함
            total_area += 1

print(total_area)


