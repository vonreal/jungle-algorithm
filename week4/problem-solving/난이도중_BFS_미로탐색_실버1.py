# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []

# map 세팅하기
for _ in range(N):
    line = []
    for data in input().rstrip():
        line.append(int(data))
    maps.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():    
    q = deque()
    visited_set = set()
    q.append((0,0,1))
    visited_set.add((0,0))

    distance = 1

    while q:
        x, y, distance = q.popleft()
        if x == N-1 and y == M-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            add_distance = distance + 1

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maps[nx][ny] == 0:
                continue
            if (nx, ny) not in visited_set:
                q.append((nx,ny,add_distance))
                visited_set.add((nx,ny))

    print(distance)

bfs()