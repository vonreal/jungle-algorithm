# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [0] * (K + 1)

for weight, value in items:
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j-weight] + value)

print(dp[K])

'''
입력)
N: 물품의 수 (1 ~ 100)
K: 버틸 수 있는 무게 (1 ~ 100,000)
W: 물건의 무게 (1 ~ 100,000)
V: 물건의 가치 (0 ~ 1,000)
무게 W, 가치 V

구하는 것)
배낭에 넣을 수 있는 물건들의 가치합의 최댓값

선택하는 것)
물건 근데 가치가 가장 큰 물건

점화식)
dp에 무게별로 최대 가치합을 저장한다.
그리고 dp[무게] = max(K-무게의 값 + 현재값)
'''