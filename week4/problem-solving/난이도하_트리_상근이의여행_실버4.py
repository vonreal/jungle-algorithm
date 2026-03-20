# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N, M = map(int, input().split())
    
    for _ in range(M):
        input()

    result.append(str(N-1))

print("\n".join(result))


'''
시간 제한: 1초
메모리 제한: 256 MB

0. 조건
    - 가장 적은 종류의 비행기를 타고 모든 국가 여행
    - 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐도 됨 (이미 방문한 국가라도)
    - 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.
1. Constraints
    입력범위)
        - T: 테스트 케이스의 수 (100 이하)
        - N: 국가의 수 (2~1,000)
        - M: 비행기의 종류 (1~10,000)
        - a,b 쌍: a와 b를 왕복하는 비행기 (1 ≤ a, b ≤ n; a ≠ b) 
    출력범위)
        테스트 케이스 수만큼 한 줄 출력: 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수 출력
2. Ideas
    1) 연결된 그래프라면 항상 N-1개가 최소값이 된다.
3. Complexity
    Idea 1)
        시간복잡도: O(T x M)
        공간복잡도: O(1) 출력제외

- 내가 모르겠는 것
    1) 연결 그래프를 이룬다.라는 말의 의미
        : 그래프 이론에서 "어떤 두 정점(노드) 사이에도 반드시 경로가 존재한다"는 의미 대표적) Tree

'''