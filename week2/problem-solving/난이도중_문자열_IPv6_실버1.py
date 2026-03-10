# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

before_ipv6 = input().split(':')
origin_ipv6 = list('0000:0000:0000:0000:0000:0000:0000:0000')

current_index = 0
flag = False

for index, ipv6 in enumerate(before_ipv6):
    if not flag and ipv6 == '':
        current_index += abs(5 * (8 - len(before_ipv6) + 1))
        flag = True
        continue

    for i, c in enumerate(reversed(ipv6)):
        if c == '':
            continue
        origin_ipv6[current_index + (3 - i)] = c
    current_index += 5

print("".join(origin_ipv6))


'''
[Algorithm Design Canvas]
전제조건: Python 사용, 1초 10^7 연산 기준 (1000만번)

1. Constraints
    1) 입력범위
        -> IPv6 주소 최대 39글자

        -> 앞자리의 0의 전체 또는 일부를 생략 할 수 있다.
        -> 0으로만 이루어져 있는 그룹은 한 개 이상 연속된 그룹을 :: 콜론 2개로 바꿀 수 있다.
    2) 출력범위
        -> 40글자의 축약되지 않은 형태
    3) Brute Force 가능한가?

2. Ideas
    1) 
        0000:0000:...:0000 으로 초기화 된 32자리 + ':' 8자리 원본 데이터를 선언한다.
        입력값을 ':'기준으로 split해서 2차원 배열로 저장한다.
        
        ':'이 나올때까지 읽고 index 기반으로 값을 대입해준다.
        ':'이 나오고 ''을 읽었다면 8 - 현재 before_ipv6의 길이 - 처리한 구간을 해서 그만큼 구간을 건너뛴다.

3. Complexities
    Idea 1) 

4. Code
5. Test

6. 개선 포인트 with AI
'''