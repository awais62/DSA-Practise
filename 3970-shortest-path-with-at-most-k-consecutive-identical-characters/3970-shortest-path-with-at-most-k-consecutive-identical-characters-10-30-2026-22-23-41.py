import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        # Priority queue stores (weight, node, consecutive_count)
        # Start at node 0 with weight 0 and count 1 (since labels[0] is the start)
        pq = [(0, 0, 1)]
        
        # Dictionary to store the minimum weight to reach a particular (node, count) state
        dist = {}
        dist[(0, 1)] = 0
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, return the shortest weight
            if u == n - 1:
                return w
            
            # If we already found a better path to this state, skip
            if dist.get((u, count), float('inf')) < w:
                continue
            
            for v, weight in adj[u]:
                # Determine the next consecutive count
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                
                # Prune invalid transitions exceeding k consecutive characters
                if next_count > k:
                    continue
                
                next_weight = w + weight
                if next_weight < dist.get((v, next_count), float('inf')):
                    dist[(v, next_count)] = next_weight
                    heapq.heappush(pq, (next_weight, v, next_count))
        
        return -1