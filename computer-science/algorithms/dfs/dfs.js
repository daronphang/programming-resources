// https://leetcode.com/problems/freedom-trail/

var findRotateSteps = function (ring, key) {
  let initialCount = key.length;
  const dp = [];

  for (let i = 0; i < key.length; i++) {
    dp[i] = Array(ring.length).fill(-1);
  }

  function dfs(index, start) {
    if (index >= key.length) return 0;
    if (dp[index][start] !== -1) return dp[index][start];

    let stepCount;
    let minCount = Infinity;

    for (let i = index; i < key.length; i++) {
      for (let j = 0; j < ring.length; j++) {
        if (key[i] === ring[j]) {
          // for same letter, there may be multiple choices
          if (j > start) stepCount = Math.min(j - start, ring.length - j + start);
          else stepCount = Math.min(start - j, ring.length - start + j);
          stepCount += dfs(i + 1, j);

          minCount = Math.min(minCount, stepCount);
        }
      }
      dp[index][start] = minCount;
      return minCount;
    }
  }

  return initialCount + dfs(0, 0);
};
