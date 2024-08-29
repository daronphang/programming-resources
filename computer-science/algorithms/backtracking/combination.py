# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(candidates, 0, [], target, ans)
        return ans

    
    def backtrack(self, candidates, start, curArr, rem, ans):
        for i in range(start, len(candidates)):
            newRem = rem - candidates[i]
            if newRem < 0: 
                return
            
            curArr.append(candidates[i])
            if newRem == 0:
                ans.append([x for x in curArr])
                curArr.pop()
                return
            
            self.backtrack(candidates, i, curArr, newRem, ans)
            curArr.pop()
        return
            