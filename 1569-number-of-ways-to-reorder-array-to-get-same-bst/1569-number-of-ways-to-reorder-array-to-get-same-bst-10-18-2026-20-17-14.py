import math


class Solution:

  def numOfWays(self, nums: list[int]) -> int:
    MOD = 10**9 + 7

    def dfs(arr):
      if len(arr) <= 2:
        return 1

      root = arr[0]
      left = [x for x in arr if x < root]
      right = [x for x in arr if x > root]

      # Ways to arrange left and right subtrees independently
      ways_left = dfs(left)
      ways_right = dfs(right)

      # Number of ways to interleave left and right elements
      comb = math.comb(len(left) + len(right), len(left))

      return (comb * ways_left * ways_right) % MOD

    # Subtract 1 because the question asks for reorderings (excluding the original array)
    return (dfs(nums) - 1) % MOD