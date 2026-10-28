class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR path values reaching (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue
                
                # Try moving right
                if j + 1 < n:
                    next_val = grid[i][j + 1]
                    for val in dp[i][j]:
                        dp[i][j + 1].add(val ^ next_val)
                        
                # Try moving down
                if i + 1 < m:
                    next_val = grid[i + 1][j]
                    for val in dp[i][j]:
                        dp[i + 1][j].add(val ^ next_val)
                        
        return min(dp[m - 1][n - 1])