# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque
import sys
input = sys.stdin.readline

# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 인접 행렬 초기화 O(N)
for _ in range(M):
    n, v = map(int, input().split())
    graph[n].append(v)
    graph[v].append(n)

# 정렬 O(N)
for i in range(1, N+1):
    graph[i].sort()

# DFS
def dfs(start, result, visited_set):
    result.append(start)
    visited_set.add(start)
    for adj_node in graph[start]:
        if adj_node not in visited_set:
            dfs(adj_node, result, visited_set)
    return result

# BFS
def bfs(start, result):
    q = deque()
    visited_set = set()

    q.append(start)
    visited_set.add(start)

    while q:
        v = q.popleft() 
        result.append(v)
        for adj_node in graph[v]:
            if adj_node not in visited_set:
                q.append(adj_node)
                visited_set.add(adj_node)
    return result

print(*dfs(V, [], set()))
print(*bfs(V, []))


