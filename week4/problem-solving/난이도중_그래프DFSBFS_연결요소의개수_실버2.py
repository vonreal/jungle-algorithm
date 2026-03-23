# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
visited[0] = True

for _ in range(M):
    n, v = map(int, input().split())
    graph[n].append(v)
    graph[v].append(n)

def bfs(start):
    global visited

    q = deque()
    
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        for adj_node in graph[v]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True

connected_count = 0
for idx, value in enumerate(visited):
    if not value:
        bfs(idx)
        connected_count += 1

print(connected_count)

