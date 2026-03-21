# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
result = defaultdict(list)
rest_node = m - 2
last_node = 0

for node in range(1, (n - rest_node)):
    result[node-1].append(node)

for i in range(rest_node):
    result[1].append((n - rest_node) + i)

for key, value in result.items():
    for ele in value:
        print(key, ele)


'''
시간제한: 2초
메모리제한: 512 MB

0. 조건
    - 트리는 사이클이 없는 연결 그래프
    - 리프는 차수가 1인 노드

1. Constraints
    입력)
        n: 노드 (3 ~ 50)
        m: 리프 (2 ~ 49)
    출력)
        n-1개의 줄에 트리의 간선 정보 출력
        정점은 0번 ~ n-1번

2. Ideas
    1) 최소 리프는 2개, 모든 노드가 일자로 연결되어있을때
        -> 리프가 하나 추가된다면 n - (m - 2)개만 일자로 연결하고 남은 노드는 리프가 아닌 요소에 붙여준다.
        -> 어떤 자료구조를 써야할까?
            배열
            0: [1]
            1: [2, 4, 5]
            2: [3]

            출력
            0 1
            1 2
            1 4
            1 5
            2 3

3. Complexity
    Idea 1)
        시간복잡도: O(N)
        공간복잡도: O(N)

+. 이해가 되지 않는 개념
    - 리프가 무엇인가?
    : 리프(leaf) = 자식이 없는 노드 = 나뭇잎

    - 간선 정보를 출력하라는 것은 무엇인가?
    : "a b" = a번 노드와 b번 노드가 연결되어 있다

    - 차수가 무엇인가?
    : degree = 그 노드에 연결된 간선의 수
'''