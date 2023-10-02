## Combination Problems

For simple problems, can use backtracking approach.

For harder problems, try to use a decision tree to work out and see if repeated sub-problems can be resolved using DP. Break down the problems into smaller subproblems, use divide and conquer approach.

## Permutation Problems

Iterate through each element in the array and add to existing dp i.e. use the results from previous iteration for the next.

## Predefined Checks

If the checks are determined i.e. tic-tack-toe (3 rows, 3 columns, 2 diagonals), can initialize the checks and iterate through them.

## Two Pointers Approach

Check if sorting will help. Pointers can either move together (tortoise and hare approach) or one pointer at a time.

For sum problems, can sort the array and take the **first and last numbers** and iterate them as necessary i.e. if sum is less than target, increment first pointer.

## DP Problems

Common characteristic of DP problems is asking for optimum value (max/min), or the number of ways there are to do something. Another characteristic is that future decisions depend on earlier decisions.

For a more intuitive approach, try reducing the number of dp objects required by **taking the difference or remainder**. The problem can then be iterated by increasing the count or size. For alternating choice problems that requires finding the maximum, use subtraction instead of addition.

**Most dp problems require initialization**; need to deduce what can be initialized/set as default value.

```py
for i in range(len(nums)):
    for j in range(i):
        # do some calc
        pass
```

### Harder Difficulty

For harder DP problems, can split into two smaller problems. Iterate the second problem and add the solution to the first problem if conditions are valid.

```
19930613    k = 1000
dp[3] = '199' = 4

199 3       3 is valid; add dp[3] to dp[4]
199 30      30 is valid, add dp[3] to dp[5]
199 306     306 is valid, add dp[3] to dp[6],6,4
```

## Greeedy Problems

For problems that will result in TLE if DP approach is used, try using greedy.

## Stacks

Common characteristic will involve having left, center and right **boundaries**, making use of monotonic increasing/decreasing stack i.e. largest area in histogram. Can be combined with DP to cache the boundaries after each iteration, or require iteration from left-to-right and right-to-left.

Another characteristic is finding the output given an input, a condition and **order is preserved** i.e. checking for closing brackets, removing duplicates in lexicographical order, etc.

## O(1) Time Complexity

For problems involving arrays that require O(1) time complexity, instead of iterating, can perform swapping to maintain time and space. Need to consider edge cases i.e. swapping last element with itself.

## O(1) Space Complexity

Can utilize the following:

- pointers (tortoise and hare)
- binary search (counting elements less than or equal to mid)
- swapping elements in array if they are not sorted i.e. nums[0] with nums[nums[0]]

## 2x2 Matrices

If you want to iterate through each column, can unpack array for Python.

```py
# [[1,2].[3,4]] becomes zip([1,2],[3,4]) and col returns (1,3), (2,4)
for col in zip(*matrix):
    pass
```

## Graphs

Check if it is bidirectional i.e. x is a neigbhor of y, and y is a neighbor of x. Common solutions are DFS.

### Shortest Path

Whenever you encounter a problem to find the shortest path in the graph, we apply **bfs** as it guarantees us to return the minimum value.
