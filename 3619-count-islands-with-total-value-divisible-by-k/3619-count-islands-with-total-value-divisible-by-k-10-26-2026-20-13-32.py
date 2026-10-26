from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        valid_islands_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    # Start BFS for the new island
                    island_sum = 0
                    queue = deque([(i, j)])
                    
                    island_sum += grid[i][j]
                    grid[i][j] = 0  # Mark as visited
                    
                    while queue:
                        r, c = queue.popleft()
                        
                        # Check all 4 directions: up, down, left, right
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                                
                    # Check if the total value of the island is divisible by k
                    if island_sum % k == 0:
                        valid_islands_count += 1
                        
        return valid_islands_count