# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.readline

target = input().split('-')
result = 0

result = int(sum(map(int, target[0].split('+'))))

for datas in target[1:]:
    result -= sum(map(int, datas.split('+')))

print(result)