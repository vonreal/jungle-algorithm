# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

coin_count = 0
while K > 0:
    temp_count = 0
    use_coin = coins.pop()
    temp_count += K // use_coin
    K -= temp_count * use_coin

    coin_count += temp_count

print(coin_count)

'''
K원을 만드는데 필요한 동전 개수의 최솟값
가장 큰 동전액수부터 시작해서 깎아내린다.
'''