# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

# 첫 풀이
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

max_num = float('-inf')

visited_index = [False] * N

def backtrack(combination, total):
    global max_num
    temp = 0

    if len(combination) == N:
        if max_num < total:
            max_num = total
        return

    for index, num in enumerate(A):
        if visited_index[index]:
            continue
        combination.append(num)
        temp = abs(combination[len(combination) - 2] - combination[len(combination) - 1]) if len(combination) > 1 else 0
        visited_index[index] = True
        backtrack(combination, total + temp)
        combination.pop()
        visited_index[index] = False
    
backtrack([], 0)
print(max_num)

# 개선 풀이
visited = [False] * N
answer = 0

def sol2():
    def backtrack2(depth, prev, total):
        global answer

        if depth == N:
            answer = max(answer, total)
            return
        
        for i in range(N):
            if visited[i]:
                continue

            visited[i] = True
            
            if depth == 0:
                backtrack2(depth + 1, A[i], total)
            else:
                backtrack2(depth + 1, A[i], total + abs(prev - A[i]))

            visited[i] = False

    backtrack2(0,0,0)
    print(answer)


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> N개의 정수: 3~8 최댓값은 8
        -> 배열 A: N개의 정수 요소는 -100~100 사이 최댓값은 100
    2) 출력범위
        -> 요소에서 순서를 바꿔 얻을 수 있는 최댓값
    3) Brute Force 가능한가?
        -> 8*8 = 64 가능

2. Ideas
    1) 백트래킹 - 순열 사용해서 진행 O(8!)해서 최댓값 진행
        - 선택: 배열 요소 하나하나, 이미 선택한 값은 선택 불가
        - 탐색: 요소 하나 하면 더할 수 있는 모든 경우
        - 취소: N개까지 골랐을때
        - 가지치기: 요소에 들어있는 값을 선택하려할때 pass

3. Complexities
    Idea 1) O(N!) => 최대가  8! = 40320

4. Code
5. Test

6. 개선 포인트 with AI
'''