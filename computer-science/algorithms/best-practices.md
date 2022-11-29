## Combination Problems

Try to use a decision tree to work out and see if repeated sub-problems can be resolved using DP. Break down the problems into smaller subproblems, use divide and conquer approach.

## Predefined Checks

If the checks are determined i.e. tic-tack-toe (3 rows, 3 columns, 2 diagonals), can initialize the checks and iterate through them.

## DP Problems

Common characteristic of DP problems is asking for optimum value (max/min), or the number of ways there are to do something. Another characteristic is that future decisions depend on earlier decisions.

```py
for i in range(len(nums)):
    for j in range(i):
        # do some calc
        pass
```

## Stacks

Common characteristic will involve having left, center and right boundaries, making use of monotonic increasing/decreasing stack i.e. largest area in histogram. Can be combined with DP to cache the boundaries after each iteration, or require iteration from left-to-right and right-to-left.

## O(1) Time Complexity

For problems involving arrays that require O(1) time complexity, instead of iterating, can perform swapping to maintain time and space. Need to consider edge cases i.e. swapping last element with itself.

## 2x2 Matrices

If you want to iterate through each column, can unpack array for Python.

```py
# [[1,2].[3,4]] becomes zip([1,2],[3,4]) and col returns (1,3), (2,4)
for col in zip(*matrix):
    pass
```
