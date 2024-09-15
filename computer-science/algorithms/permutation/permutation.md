## Permutation

Use the results from the previous computed sequence to generate the new results with the next value.

```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize
        prev = [[nums[0]]]
        cur = []

        for idx, x in enumerate(nums):
            if idx == 0: continue

            for arr in prev:
                for i in range(len(arr) + 1):
                    temp = arr[:i] + [x] + arr[i:]
                    cur.append(temp)

            prev = cur
            cur = []

        return prev
```
