# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())
    ranks = []

    # 서류, 면접 순위
    for i in range(N):
        grade1, grade2 = map(int, input().split())
        ranks.append((grade1, grade2))
    
    ranks.sort(key=lambda x:x[0])
    minimum = ranks[0][1]
    pass_total = 1
    
    for rank1, rank2 in ranks[1:]:
        if rank2 < minimum:
            pass_total += 1
            minimum = rank2
    result.append(str(pass_total))
    
print("\n".join(result))



'''
입력)
T: 테스트 케이스 (1~20)
N: 지원자의 숫자 (1~100,000)
지원자의 서류심사 성적, 면접 성적의 순위

출력)
- 서류심사 성적 or 면접 성적이 다른 지원자보다 떨어지지 않는 자만 선발 (둘 다 떨어지면 miss)
선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램


다른 사람의 순위를 알고 있어야 함
-> 근데 순위는 서류, 면접 성적임
-> 서류, 면접 성적 둘 중 하나라도 다른 사람보다 크면 됨

그리디도 필요한듯 . 지금 내가 보고 있는 사람이 가장 최선이라고 생각.
그리고 

상태: 
초기값:
점화식:

'''