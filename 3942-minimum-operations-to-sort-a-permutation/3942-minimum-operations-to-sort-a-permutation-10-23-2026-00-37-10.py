class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        want = list(range(n))
        i = nums.index(0)
        
        # Check if it's a valid increasing rotation
        if nums[i:] + nums[:i] == want:
            return min(i, n - i + 2)
            
        # Check if it's a valid decreasing rotation
        if nums[i::-1] + nums[:i:-1] == want:
            return min(i + 2, n - i)
            
        return -1