# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

total_computers = int(input())
total_linked_computers = int(input())

adj_list = defaultdict(list)

# O(N) 인접 리스트 삽입
for _ in range(total_linked_computers):
    n, v = map(int, input().split())

    adj_list[n].append(v)
    adj_list[v].append(n)

def bfs(n):
    queue = deque()
    visited_set = set()

    queue.append(n)
    visited_set.add(n)

    while queue:
        v = queue.popleft()
        for adj_node in adj_list[v]:
            if adj_node not in visited_set:
                queue.append(adj_node)
                visited_set.add(adj_node)

    print(len(visited_set) - 1)

bfs(1)

