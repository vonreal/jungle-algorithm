# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

T = int(input())
result = [0] * T

for test_index in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for price in range(coin, M + 1):
            dp[price] += dp[price - coin]

    result[test_index] = str(dp[M])

print("\n".join(result))


'''
모든 방법을 세는 방법

입력)
T: 테스트 케이스의 개수 (1 ~ 10)
N: 동전의 가지 수 (1 ~ 20)

출력)
N가지 동전으로 금액 M을 만드는 모든 방법의 수

1. 뭘 구하는가?
N가지 동전으로 금액 M을 만드는 모든 방법의 수

2. 어떤 알고리즘을 선택하는가?
모든 경우의 수: DP, BFS, 백트래킹 (입력값 오버)

3. 매핑
- 저장해야하는 데이터 혹은 부분합으로 접근

30원을 만드는 법
1원, 5원, 10원
1원 * 30개
5원 1개, 1원 * 25개
5원 2개, 1원 * 20개
5원 3개, 1원 * 15개
5원 4개, 1원 * 10개
5원 5개, 1원 * 5개
5원 6개
10원 1개 + total[20]
10원 2개 + total[10]
10원 3개 + total[0]


1원을 만드는 경우의 수
2원을 만드는 경우의 수
저장할 데이터는 금액을 만드는 경우의 수!
최솟값부터 시작해서

coins의 처음 값부터 시작해서 이전의 값(남은 금액)을 누적해서 가짓수를 저장한다.

상태: 1원부터 ~ M까지 반복
이웃: coins의 처음부터 끝까지 돌면서 가능한 조합 모두 처리

"한 번에 하나의 선택만 한다"는 DP의 사고 전환
'''
