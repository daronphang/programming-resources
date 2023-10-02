## Traversing BST

There are different ways of traversing a binary tree, depending on the order that the nodes are are visited: in-order, pre-order, and post-order.

### In-Order

You traverse from the left subtree to the root then to the right subtree.

```
inOrder(x) {
    if x != NIL
        inOrder(x.left)
        print(x.key)
        inOrder(x.right)
}
```

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        // in-order traversal

        int[] ans = dfs(root, new int[]{0,-1}, k);
        return ans[1];
    }

    public int[] dfs(TreeNode node, int[] pair, int k) {
        if (node == null) return pair;
        int[] rv = null;

        // traverse left
        rv = dfs(node.left, pair, k);

        // kth smallest element has been found
        if (rv[1] != -1) return rv;

        // update pair and check
        rv[0] += 1;
        if (rv[0] == k) {
            rv[1] = node.val;
            return rv;
        }

        // traverse right
        return dfs(node.right, rv, k);
    }
}
```

### Pre-Order

You traverse from the root to the left subtree then to the right subtree.

### Post-Order

You traverse from the left subtree to the right subtree and then to the root.
