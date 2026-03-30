# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
from collections import deque
import sys
input = sys.stdin.readline

stone_count, broken_count = map(int, input().split()) # 전체 돌의 개수, 밟을 수 없는 돌의 개수

broken_stones = set()
for _ in range(broken_count):
    broken_stones.add(int(input()))

def solve_dfs():
    q = deque()
    visited = set()
    result = -1

    if 2 not in broken_stones:
        q.append((2, 1, 1)) # 돌 위치, 속도, 점프 총합
        visited.add((2, 1))
    
    
    while q:
        stone, speed, jumps = q.popleft()
        if stone == stone_count:
            result = jumps
            break
        for distance in range(-1, 2):
            new_speed = speed + distance
            new_stone = stone + new_speed
            
            if new_speed < 1 or new_stone < 1 or new_stone > stone_count:
                continue
            if new_stone in broken_stones:
                continue
            if (new_stone, new_speed) in visited:
                continue
            q.append((new_stone, new_speed, jumps + 1))
            visited.add((new_stone, new_speed))

    print(result)

def solve_dp():
    MAX_JUMP_SIZE = 150
    INF = float("inf")

    # dp[돌 번호][점프 크기] = 최소 점프 횟수
    dp = [[INF] * (MAX_JUMP_SIZE + 1) for _ in range(stone_count + 1)]

    result = -1
    if 2 not in broken_stones:
        dp[2][1] = 1
        for stone in range(2, stone_count + 1):
            if stone in broken_stones:
                continue
            for jump_size in range(1, MAX_JUMP_SIZE + 1):
                if dp[stone][jump_size] == INF:
                    continue
                # 다음 점프
                for delta in range(-1, 2):
                    next_jump_size = jump_size + delta
                    next_stone = stone + next_jump_size
                    if next_jump_size < 1 or next_stone > stone_count:
                        continue
                    if next_stone in broken_stones:
                        continue
                    dp[next_stone][next_jump_size] = min(
                        dp[next_stone][next_jump_size],
                        dp[stone][jump_size] + 1
                    )
    result = min(dp[stone_count][1:])
    print(result if result != INF else -1)

solve_dfs()
# solve_dp()


    

'''
N개의 돌 (2 ~ 10,000)

구하는 것: 1번 돌에서 N번 돌까지 점프를 해 갈 때, 필요한 최소의 점프 횟수
갈 수 없는 경우 -1

최소횟수 => BFS, DP

[조건]
- 맨 처음에는 한 칸 밖에 점프 불가능

[BFS]
상태: (위치, 속도)
이웃: 현재위치에서 내가 점프할 수 있는 칸
거리: x-1, x, x+1
목표: 최소의 점프 횟수

[DP]
상태: 돌과 속도(x칸 점프), dp[돌][마지막 점프 크기] = 최소 점프 횟수
점화식: 돌(i), 점프 크기(k) dp[i + (k - 1)][k-1], dp[i + k][k], dp[i + (k + 1)][k+1]
초기값: dp[2][1] = 1
방향: bottom-up
'''