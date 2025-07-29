import sys

n = int(sys.stdin.readline()) # 컴퓨터 수
m = int(sys.stdin.readline()) # 네트워크 수

graph = [[] for _ in range(n+1)]

# 그래프 구성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    count = 1
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor)
    return count

print(dfs(1) - 1)