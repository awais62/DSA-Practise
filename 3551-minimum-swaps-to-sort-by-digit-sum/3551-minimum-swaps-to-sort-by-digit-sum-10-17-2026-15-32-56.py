class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        n = len(nums)
        # Pair each number with its original index
        arr = [(nums[i], i) for i in range(n)]
        
        # Sort by digit sum first, then by numerical value as a tie-breaker
        arr.sort(key=lambda x: (digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or arr[i][1] == i:
                continue
            
            # Find the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][1]
                cycle_size += 1
            
            # Add swaps required for this cycle
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        Info = swaps
        return swaps        
