## Simulation

Using stacking of glasses in a pyramid as a problem, we are asked to find how much champagne is a certain number of glasses is poured from the top glass. Instead of keeping track how much champagne should end up in a glass, **keep track of the total amount of champagne that flows through a glass** i.e. the remainder after filling up the current glass.

https://leetcode.com/problems/champagne-tower/editorial/?envType=daily-question&envId=2023-09-24

```java
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] dp = new double[100][100];
        dp[0][0] = poured;
        double flow = 0;

        for (int i = 0; i < query_row; i++) {
            for (int j = 0; j <= i; j++) {
                // amount will be divided equally between left and right
                flow = (dp[i][j] - 1) / 2;
                if (flow < 0) continue;
                dp[i+1][j] += flow;
                dp[i+1][j+1] += flow;
            }
        }
        return Math.min(1, dp[query_row][query_glass]);
    }
}
```
