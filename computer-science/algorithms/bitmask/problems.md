## Problem 1

Given a set of N people and N tasks, you have to assign 1 task to exactly 1 person. This means that every person will be allotted only one task.

Out of all the possible combinations in which the tasks can be allotted, we have to assign the tasks in such a way that the total cost of assigning the tasks is maximized.

```
[
    [2,9,7],
    [6,4,3],
    [1,8,5],
]
```

```c++
#include<bits/stdc++.h>
using namespace std;

int N;
int Cost[21][21];

int Maximum_Cost(int i, int mask)
{
	if (i >= N)
	{
		// base case
		return 0;
	}

	// As we need the maximum answer assign ans with the minimum
	// integer value.
	int ans = INT_MIN;

	for (int k = 0; k < N; k++)
	{
		//Check if the k-th person has been already assigned a
		//task or not.
		if ((mask & (1 << k)) == 0)
		{
			//if k-th person has not been assigned a task,
			//add Cost[i]][k] and make the k-th bit of mask=1
			//Solve the recursion to assign i+1-th job with set
			//of people represented by the mask value.

			ans = max(ans, Cost[i][k] + Maximum_Cost(i + 1, (mask | (1 << k))));
		}
	}

	// return the optimal answer for the current state.

	return ans;
}

int main()
{

	N = 3;

	// input is same as discussed in the problem statement
	//{{2,9,7},
	// {6,4,3},
	// {1,8,5}}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> Cost[i][j];
		}
	}

	//Print the maximum cost for assigning the tasks
	cout << "Optimal Solution for the given N and Cost Matrix is:\n";
	cout << Maximum_Cost(0, 0);

	return 0;
}

```

## Problem 2

https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/?envType=daily-question&envId=2023-09-17

```java
import java.util.*;

class Solution {
    class Node {
        int node;
        int mask;
        int cost;

        Node(int node, int mask, int cost) {
            this.node = node;
            this.mask = mask;
            this.cost = cost;
        }
    }

    public int shortestPathLength(int[][] graph) {
        // bfs + bitmask
        int n = graph.length;
        int all = (1 << n) - 1;
        Set<Pair<Integer, Integer>> vis = new HashSet<>();
        Queue<Node> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            int maskValue = (1 << i);
            Node thisNode = new Node(i, maskValue, 1);
            q.add(thisNode);
            vis.add(new Pair<>(i, maskValue));
        }

        while (!q.isEmpty()) {
            Node curr = q.poll();

            if (curr.mask == all) {
                return curr.cost - 1;
            }

            for (int adj : graph[curr.node]) {
                int bothVisitedMask = curr.mask | (1 << adj);
                Node thisNode = new Node(adj, bothVisitedMask, curr.cost + 1);

                if (!vis.contains(new Pair<>(adj, bothVisitedMask))) {
                    vis.add(new Pair<>(adj, bothVisitedMask));
                    q.add(thisNode);
                }
            }
        }

        return -1;
    }
}
```

## Problem 3

Given a non-empty array of integers, every element appears twice except for one. Find that single one. Your algorithm should have a linear runtime complexity, without using extra memory.

The solution is using XOR. If you XOR identical numbers, the result will be 0.

```py
def single_number(list):
  result = 0
    for num in list:
      result ^= num
  return result

'''
[4,1,2,1,2]
4 = 100
1 = 001
2 = 010

0 ^ 4 = 0 ^ 100 = 4
4 ^ 1 = 100 ^ 001 = 101 = 5
5 ^ 2 = 101 ^ 010 = 111 = 7
7 ^ 1 = 111 ^ 001 = 110 = 6
6 ^ 2 = 110 ^ 010 = 100 = 4
'''
```
