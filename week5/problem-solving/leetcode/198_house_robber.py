class Solution:
    # 아래 케이스를 보완하기 위해서
    # 그러면 인접하지 않은 첫 번째 집을 턴게 아니라
    # 인접하지 않은 두 번째 집을 턴 값을 비교해서 큰 값으로 처리해보자.
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = nums[1]

        for index, num in enumerate(nums[2:], start=2):
            dp[index] = max((dp[index - 2] + num), dp[index - 3] + num)

        return max(dp)
    # 개선점: dp에 저장하는 값을 애초에 인접하지 않은 값 중 최댓값만 저장하게 했어야 올바른 접근법인 것 같음.
    # 현재 나는 통과 했지만 3박자가 잘 떨어져서 돌아갔던 것.


    # 내가 처음에 생각했던 방향.
    # 인접하지 않은 집을 털었을때의 값을 지금 값과 더하면 인접하지 않은 집을 턴 돈이 있을텐데,
    # 그러면 max(dp)를 하면 인접하지 않은 집을 털었을 때 경우 중 가장 많이 턴 집을 알 수 있지 않았을까?
    # 실패 케이스: 2, 1, 1, 2 일 경우
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = nums[1]

        for index, num in enumerate(nums[2:], start=2):
            dp[index] = dp[index - 2] + num

        return max(dp)



'''
- 인접한 집들에 보안 시스템이 연결되어있음
- 같은 날 밤에 인접한 집에 침입하면 경찰에 신고됨

입력)
nums: 각 집의 돈

출력)
경찰에 들키지 않고 얻을 수 있는 가장 많은 돈

점화식: dp[i] = dp[i - 2] + nums[i]

0, 1, 2, 3
1 2 3 1
0 + 2
1 + 3

0, 1, 2, 3


2, 1, 1, 2 (마지막 ㅇ)
수정 점화식: dp[i] = max((dp[i - 2] + nums[i]), (dp[i - 3] + nums[i]))

현재가 마지막일때 -2, -3 둘 중 더 큰 경우로 진행 (왜냐면 인접한 요소 중에서 한단계 건너뛸 수도 있으니까.)
이전일때는 그냥 과거에 있을거라고 믿고 진행.
'''