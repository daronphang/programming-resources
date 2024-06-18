## Binary Search

Can use binary search with divide and conquer strategy. Only works if list is sorted. Has time complexity of O(log2n) as compared to linear with O(n).

```py
def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + floor((right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    if nums[left] == target: return left
    return -1
```

```py
def binary_search(self, candidates, target):
    # return idx of element that is largest in list but smaller than target
    # i.e. idx+1 element is larger than target and cannot be used in sum
    mid = len(candidates) // 2
    left = 0
    right = len(candidates) - 1

    while left < right:
        if candidates[mid] == target:
            # since all elements are distinct, can stop here
            break
        elif candidates[mid] < target:
            # continue checking on right as there may exist an element that meets criteria
            left = mid
            mid = left + (right-left + 1) // 2
        else:
            # element > target, find next valid element
            right = mid - 1
            mid = left + (right-left) // 2

    return mid
```

### Binary Search on Numbers (Given Index)

```py
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left < right:
            count = 0
            mid = (right+left) // 2

            for i in range(n):
                # count how many elements are less than mid
                # perform binary search for each row
                count += bisect_right(matrix[i], mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
```

```py
def binary_search(arr, k):
    left = arr[0]
    right = arr[len(arr)-1]


    while left < right:
        mid = (left+right) // 2

        if mid > k:
            right = mid
        elif mid < k:
            left = mid + 1
        else:
            break

    return mid

print(binary_search([1,4,6,8,9,10,12,15,25,30,45,50], 45))
```

## Pigeonhole principle with Binary Search

Problem:

- Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive
- There is only one repeated number in nums, return this repeated number
- You must solve the problem without modifying the array nums and uses only constant extra space

Can combine pigeonhole principle with binary search i.e. counting the number of elements less than or equal to a number.

https://leetcode.com/problems/find-the-duplicate-number/solutions/?envType=daily-question&envId=2023-09-19

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int start = 0;
        int end = nums.length - 2;

        while (start < end) {
            // count the numbers that are <= mid
            int mid = start + (int) Math.floor((end - start) / 2);


            if (countNumber(nums, mid) > mid) end = mid;
            else start = mid + 1;
        }

        if (countNumber(nums, start) > start) return start;
        return start + 1;
    }

    public int countNumber(int[] nums, int v) {
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= v) counter += 1;
        }
        return counter;
    }
}
```
