# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input()) # 보드의 크기
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input()) # 사과의 개수
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input()) # 뱀의 방향 변환 횟수

snake = deque() # 뱀
result = 0 # 초
x = y = 0

# 우, 하, 좌, 상 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0 # 처음엔 오른쪽

turns = defaultdict()
body_set = set()

for _ in range(L):
    parts = input().split()
    turns[int(parts[0])] = parts[1]

snake.append((0,0))
body_set.add((0,0))

while True:
    result += 1

    x += dx[d]
    y += dy[d]

    # 벽에 충돌
    if x < 0 or y < 0 or x == N or y == N:
        break

    # 내 몸에 충돌
    if (x, y) in body_set:
        break

    snake.append((x,y))
    body_set.add((x,y))

    # 사과 먹을 때 꼬리 처리
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        tail = snake.popleft()
        body_set.remove(tail)

    if result in turns:
        if (turn := turns[result]) == 'D':
            d = (d + 1) % 4 # turn right
        else:
            d = (d - 1) % 4 # turn left

print(result)

'''
시간제한: 1초
메모리제한: 128 MB

0. 조건

1. Constraints
    입력범위:   보드의 크기 N (2 ~ 100)
                사과의 개수 K (0 ~ 100)
                뱀의 방향 변환 횟수 L (1 ~ 100)
2. Ideas
    핵심연산:
    1) 

3. Complexity
    Ideas1)
        시간복잡도:
        공간복잡도:
'''