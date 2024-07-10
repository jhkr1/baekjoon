N = int(input()) # 참가자 수
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split()) # T장씩 몇 묶음, P개씩 몇 묶음

T_list = [S, M, L, XL, XXL, XXXL]

T_result = 0

# 6개의 사이즈, 같은 사이즈 T장 묶음
# 펜은 한 종류, P자루씩 묶음

# 출력되는 첫번째 줄에는 T장씩 몇 묶음이 필요한지

for size in T_list:
    if size % T == 0:
        T_result += size // T
    else:
        T_result += (size // T) + 1

print(T_result)
print(N // P, N % P)

        

        
    