# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
K = int(input())

# V가 최대 20,000 스택 오버플로우 가능
def dfs(start, adj_list, graphs):
    for adj_node in adj_list[start]:
        if graphs[start] == graphs[adj_node]:
            return False
        if not graphs[adj_node]:
            graphs[adj_node] = graphs[start] * -1
            if not dfs(adj_node, adj_list, graphs):
                return False
    return True

def bfs(start, adj_list, graphs):
    q = deque([start])

    while q:
        v = q.popleft()
        for adj_node in adj_list[v]:
            if graphs[adj_node] == graphs[v]:
                return False
            if not graphs[adj_node]:
                graphs[adj_node] = graphs[v] * -1
                q.append(adj_node)
    return True

def isBipartiteGraph(adj_list, graphs):
    for i in range(1, len(graphs)):
        if not graphs[i]:
            graphs[i] = 1
            if not bfs(i, adj_list, graphs):
                return "NO"
    return "YES"

# 입력 값 받기, start와 인접 리스트 넘기기
for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n, v = map(int, input().split())
        adj_list[n].append(v)
        adj_list[v].append(n)
    graphs = [0] * (V + 1)
    print(isBipartiteGraph(adj_list, graphs))



'''
선수지식: 이분 그래프
- 그래프의 모든 정점이 두 그룹으로 나눠지고 서로 다른 그룹의 정점이 간선으로 
연결되어져 있는(같은 그룹에 속한 정점끼리는 서로 인접하지 않도록 하는) 그래프를 이분 그래프라고 한다.


1. 뭘 구하는가?
- 그래프가 이분 그래프인지 아닌지 판별하는 프로그램
- 
2. 입력 크기와 제약?
3. 어떤 알고리즘?
- dfs
4. 매핑
상태: 첫 노드부터 실행하기
언제까지?: 모든 노드를 탐색할때까지 (연결이 끊겨진 노드 탐색도 고려)
이웃: 나랑 인접한 노드는 다른 값을 가져야 함
'''