# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())

'''
동작
    1) 제일 위에 있는 카드를 바닥에 버린다.
    2) 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    3) 1,2를 반복하고 남는 마지막 카드를 출력하기

0. 조건
    시간 제한: 2초
    메모리 제한: 128 MB

1. Constratins
    - 입력 범위) N장의 카드: 1 ~ 500,000
    - 출력 범위) 숫자 1개

    
2. Ideas
    1) deque 사용

3. Complexity
    1) deque의 PopLeft(), pop()은 O(1) 시간복잡도는 O(N), 공간복잡도 O(N)


'''