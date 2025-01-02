# location = []
# R_location = []
# R_col_location = []
# R_row_location = []

# for _ in range(8):
#     row = input()
#     location.append(list(row))

# for i in range(8):
#     for j in range(8):
#         if(location[i][j] == 'R'):
#             R_location.append((i, j))

# for row,col in R_location:
#     R_row_location.append(row)
#     R_col_location.append(col)

# for i in range(8):
#     for col in range(len(R_col_location)):
#         location[i][R_col_location[col]] = 'R'
#     for row in range(len(R_row_location)):
#         location[R_row_location[row]][i] = 'R'


# cnt = 0
# for i in range(8):
#     for j in range(8):
#         if(location[i][j] == '.'):
#             cnt += 1

# print(cnt)
            
        
# 개선된 코드
# 입력받기
board = [input() for _ in range(8)]

# 공격받는 행과 열 추적
attacked_rows = set()
attacked_cols = set()

# R의 위치 기록
for i in range(8):
    for j in range(8):
        if board[i][j] == 'R':
            attacked_rows.add(i)
            attacked_cols.add(j)

# 안전한 칸 계산
safe_count = 0
for i in range(8):
    for j in range(8):
        if i not in attacked_rows and j not in attacked_cols:
            safe_count += 1

print(safe_count)