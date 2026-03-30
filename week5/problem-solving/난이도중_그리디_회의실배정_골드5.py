# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())    
    meetings.append((start, end))

meetings.sort(key= lambda x: (x[1], x[0]))

available_meetings = 0
before_end = 0

for start, end in meetings:
    if start >= before_end:
        before_end = end
        available_meetings += 1

print(available_meetings)