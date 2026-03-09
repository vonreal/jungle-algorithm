# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import sys
input = sys.stdin.readline

N = int(input())
cityCosts = [[int(cost) for cost in input().split()] for _ in range(N)]

minimumCost = float('inf')

def backtrak(start, visitedCity, cost):
    global minimumCost

    if minimumCost <= cost: # 비용이 minimumCost보다 크거나 같으면 검사하지 않아도 됨
        return

    if N == len(visitedCity):
        if minimumCost > (totalCost := cost + cityCosts[start][0]): # 처음 도시로 돌아가는 비용
            minimumCost = totalCost
        return
    
    for nextCity in range(N):
        if nextCity in visitedCity:
            continue
        if cityCosts[start][nextCity] == 0: # 갈 수 없는 경우
            continue

        visitedCity.add(nextCity)
        backtrak(nextCity, visitedCity, cost + cityCosts[start][nextCity])
        visitedCity.remove(nextCity)
    
backtrak(0, {0}, 0)

print(minimumCost)

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

0. 선수지식: 백트래킹 판단 절차 3단계, 개념 심화 학습 (with AI)
    1) 모든 경우를 봐야 하는가?
    2) 입력범위가 작은가?
    3) 단계별 선택 구조인가?
0-2. 백트래킹 시간복잡도 정리
    1) 순열: O(N!), N <= 11 까지만 가능
    2) 조합/부분집합: O(2^n), n<= 25까지만 가능
0-3. 순열 vs 조합 판단 기준
    1) 순서가 중요한가? -> yes:순열 / no: 조합/부분집합
0-4. 백트래킹 아이디어 정의 항목
    1) 선택: 각 단계에서 뭘 선택해?
    2) 탐색: 언제 다음 단계로 넘어가?
    3) 취소: 뭘 되돌려?
    4) 종료 조건: 언제 멈춰?
    5) 가지치기(선택): 불필요한 탐색을 어떻게 줄여?

1. Constraints
    1) 입력범위
        -> N: 도시의 수 (최솟값:2, 최댓값: 10)
        -> 행렬 성분: (최솟값:1, 최댓값: 1,000,000), 갈 수 없을 경우: 0
    2) 출력범위
        -> 외판원의 순회에 필요한 최소 비용 (양의 정수)
        -> 모든 도시를 거쳐 다시 원래 도시로 돌아와야함
        -> 0인 경우 갈 수 없는 경로임
        -> 한 번 갔던 도시로는 다시 갈 수 없음 (맨 마지막 -> 출발 도시 예외)
    3) Brute Force 가능한가?
        -> 

2. Ideas
    1) 백트래킹 사용
        -> 선택: 다음에 방문할 도시를 선택
        -> 탐색: 선택한 도시로 이동 후 비용 합산, 가지 않은 다른 도시로 이동
        -> 취소: 방문 표시를 지움
        -> 종료 조건: 모든 도시를 방문하고 시작점으로 돌아오는 비용 합산해 최소비용 반환
        -> 가지치기: 현재까지 비용이 이미 최소값보다 크면 종료

3. Complexities
    Idea 1)
        시간복잡도: 시작도시 고정이므로 O(N-1)!
        공간복잡도: O(N) - 방문 배열 + 재귀 스택

4. Code
5. Test

6. 개선 포인트 with AI
'''