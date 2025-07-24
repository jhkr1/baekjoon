import sys


def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        clothes = {}
        for _ in range(n):
            name, kind = sys.stdin.readline().split()
            # 만약 옷장에 같은 종류의 옷이 있다면 += 1
            if kind in clothes:
                clothes[kind] += 1
            # 같은 종류의 옷이 없다면 하나로 바꿔줌.
            else:
                clothes[kind] = 1
        result = 1
        for kind in clothes:
            # 안 입는 경우를 + 1
            result *= (clothes[kind] + 1)
        # 전부 안 입는 경우를 제외
        print(result - 1)


solve()
