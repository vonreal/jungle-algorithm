# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

# print((A ** B) % C) 시간초과

def custom_pow(base, top):
    if top == 0:
        return 1 % C
    
    base %= C

    if top == 1:
        return base % C
    
    half = custom_pow(base, top // 2) % C

    if top % 2 == 0:
        return (half * half) % C
    else:
        return (base * half * half % C) % C
    
print(custom_pow(A, B))


'''
시간제한: 0.5초
메모리제한: 128 mb
'''