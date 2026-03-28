# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

strA = input().rstrip()
strB = input().rstrip()

dp = [[0 for _ in range(len(strB) + 1)] for _ in range(len(strA) + 1)]

for i in range(1, len(strA) + 1):
    for j in range(1, len(strB) + 1):
        if strA[i - 1] == strB[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(strA)][len(strB)])