class Solution:
  # given an array [1,0,2,3,5,4]
  # solve [1] first, followed by [1,0], then [1,0,2]
  #each time you increment, can use results from previous iteration
  def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    ans = 1

    for i in range(len(nums)):
        for j in range(i+1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])
    return ans