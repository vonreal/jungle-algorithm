# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 2)
dp[1], dp[2] = 1, 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 15746)


'''
키워드: 모든 가짓수를 센다.

1이면 1
2면: 00, 11 2
3면: 100, 001, 111 3개
4면: 0011, 0000, 1001, 1100, 1111 5개

새로운 타일: 누적합?
점화식: dp[n] = dp[n-1] + dp[n-2]
'''