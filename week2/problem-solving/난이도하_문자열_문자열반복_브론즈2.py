# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    inputs = input().split()

    r = int(inputs[0])
    string = inputs[1]

    for char in string:
        for _ in range(r):
            print(char, end='')
    print()

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> t: 테스트 케이스 갯수는 1~1000
        -> r: 문자 반복은 최대가 8번 최소가 1번
        -> s: S의 길이는 최대가 20글자 최소가 1글자
    2) 출력범위
        -> 최대는 20 * 8 = 160이고 최소는 1
    3) Brute Force 가능한가?
        -> 가능

2. Ideas
    1) s를 하나씩 읽으면서 출력은 r번 반복한다.

3. Complexities
    Idea 1) 시간복잡도: O(r x s) -> 근데 최대가 160이기 때문에 거의 O(1), 공간복잡도: O(1) 선언하는 변수 없음.

4. Code
5. Test

6. 개선 포인트 with AI
'''