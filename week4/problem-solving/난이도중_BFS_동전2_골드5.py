# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n

# 코인 데이터 넣어두기
for i in range(n):
    coins[i] = int(input())

def bfs():
    q = deque()
    visited_set = set()

    q.append((0, 0))
    visited_set.add(0)

    count = 0

    while q:
        total, count = q.popleft()
        for coin in coins:
            add_total = total + coin
            add_count = count + 1
            if add_total == k:
                return add_count
            elif add_total > k:
                continue
            if add_total not in visited_set:
                q.append((add_total, add_count))
                visited_set.add(add_total)
    return -1
    
print(bfs())
