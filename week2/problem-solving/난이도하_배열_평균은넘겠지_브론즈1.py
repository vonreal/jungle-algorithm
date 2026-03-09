# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# Answer 코드
import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    grades = list(map(int, input().split(' ')))[1:]
    total = len(grades)
    
    grade_avg = sum(grades) / total
    count = 0
    for grade in grades:
        if grade > grade_avg:
            count += 1
            
    print(f'{(count / total) * 100:.3f}%')

'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> 테스트 케이스 개수(C) 최솟,최댓값 지정 없음
        -> 테스트 케이스 학생 수(N는 1~1000 가능, 점수는 0~100 가능
        O(C x N) -> 최대가 O(C x 1000) -> O(C)
    2) 출력범위
        -> 평균, 소수점 셋째 자리까지
    3) Brute Force 가능한가?
        -> 가능

2. Ideas
    1) 저장 없이 바로 지정된 C, N 만큼 반복문 돌면서 연산 시작

3. Complexities
    Idea 1) O(C x N), 공간복잡도 O(1)

4. Code
5. Test

6. 개선 포인트 with AI
'''