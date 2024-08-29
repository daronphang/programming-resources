 # https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        self.backtrack(nums, visited, [], ans)
        return ans
    
    def backtrack(self, nums, visited, curArr, ans):
        if len(curArr) == len(nums):
            ans.append([x for x in curArr])
            return

        for x in nums:
            if x in visited: continue
            visited.add(x)
            curArr.append(x)
            self.backtrack(nums, visited, curArr, ans)
            visited.remove(curArr.pop())
        return
            


        