class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]  # 맨 아래 행으로 초기화

        for j in range(len(triangle) - 2, -1, -1):      # 아래에서 위로
            for i in range(len(triangle[j])):
                dp[i] = triangle[j][i] + min(dp[i], dp[i + 1])

        return dp[0]

'''
위에서 아래로 내려갈때 합의 최소를 구해라?
각 열에서 가장 작은 값을 더하면 되는거 아닌가?!

아 그런데 이제 O(N)이어야한다.

- 각 단계에서 바로 아래 행의 인접한 번호로 이동할 수 있습니다. 
- 좀 더 정확하게 말하면, 현재 행의 인덱스 i에 있다면 다음 행의 인덱스 i 또는 인덱스 i + 1로 이동할 수 있습니다.

dp[j][i] = min(dp[j+1][i], dp[j+1][i+1])
'''