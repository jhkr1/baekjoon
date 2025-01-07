n, m = map(int, input().split())  # 보드 크기
board = [input() for _ in range(n)]  # 보드 입력

# 체스판 패턴 정의
chess_white_start = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

chess_black_start = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

def count_repaints(x, y):
    white_repaint = 0
    black_repaint = 0

    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess_white_start[i][j]:
                white_repaint += 1
            if board[x + i][y + j] != chess_black_start[i][j]:
                black_repaint += 1

    return min(white_repaint, black_repaint)

# 최소 칠해야 하는 칸의 수 계산
min_repaints = float('inf')

for i in range(n - 7):  # 세로로 가능한 시작 지점
    for j in range(m - 7):  # 가로로 가능한 시작 지점
        min_repaints = min(min_repaints, count_repaints(i, j))

print(min_repaints)