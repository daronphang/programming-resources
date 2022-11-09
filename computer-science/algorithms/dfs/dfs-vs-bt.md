### DFS vs Backtracking

Backtracking is a more general purpose algorithm that can be applied to any data structure. Handles an implicit tree. Backtracking can stop/finish searching certain branch if certain conditions are not met. Need to restore the previous state of visited node.

DFS is a specific form of backtracking related to searching tree structures. Handles an explicit tree. In DFS, pruning is not allowed, and you have to reach to the leaf node of the branch to figure out if the condition is met or not.

DFS is quicker than a general backtracking algorithm.
