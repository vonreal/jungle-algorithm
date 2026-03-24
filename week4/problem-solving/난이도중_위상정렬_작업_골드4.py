# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
task_times = [0] * (N+1)
indegrees = [0 for _ in range(N+1)]
adj_list = defaultdict(list)

# indegree + 인접 리스트 설정하기
for i in range(1, N+1):
    datas = list(map(int, input().split()))
    task_times[i] = datas[0]
    indegrees[i] = datas[1]
    for j in range(2, 2 + indegrees[i]):
        adj_list[datas[j]].append(i)

# 선행차수가 0인것부터 동시 실행(작업시간이 더 큰 것으로 산정해서 계산)
q = deque([i for i in range(1, N+1) if indegrees[i] == 0])

# 여기서 28번째 코드에서 큐에 들어간값 중 시간이 가장 큰 것으로 계산,나머지는 합치지 않음. 으로 생각했는데 힌트에 가까움?
task_total = 0
end_time = [0] * (N+1)
end_time.append(task_times[1])
while q:
    task = q.popleft()
    if not q:
        task_total += max(end_time)
        end_time = []
    for adj_task in adj_list[task]:
        indegrees[adj_task] -= 1
        if indegrees[adj_task] == 0:
            q.append(adj_task)
            end_time.append(task_times[adj_task])

print(task_total)




'''
1. 뭘 구하는가?
    - 모든 작업을 완료하기 위한 최소 시간
2. 입력의 크기와 제약은?
    - 선행 관계가 있음, 1번 작업은 선행 관계가 없음
    - 선행 관계가 없는 작업들은 동시 수행 가능
    - N: 3 ~ 10,000
    - 시간: 1 ~ 100
3. 어떤 구조/알고리즘이 맞는가?
    - 위상 정렬
4. 풀이
    - 노드: 작업
    - 간선: 작업번호 - 1인것들이 끝나야 시작할 수 있음
    - 진입 차수: 작업번호가 1부터 시작해야함
'''