class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        dp[0] = triangle[0][0]

        for j in range(len(triangle) - 1):
            for i in range(len(triangle[j+1]) - 1):      
                dp[j+1] = min(triangle[j+1][i], triangle[j+1][i+1])

        return sum(dp)

'''
위에서 아래로 내려갈때 합의 최소를 구해라?
각 열에서 가장 작은 값을 더하면 되는거 아닌가?!

아 그런데 이제 O(N)이어야한다.

- 각 단계에서 바로 아래 행의 인접한 번호로 이동할 수 있습니다. 
- 좀 더 정확하게 말하면, 현재 행의 인덱스 i에 있다면 다음 행의 인덱스 i 또는 인덱스 i + 1로 이동할 수 있습니다.

dp[j][i] = min(dp[j+1][i], dp[j+1][i+1])
'''