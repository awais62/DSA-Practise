class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0
        
        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        for k in divisors:
            valid = True
            for i in range(0, n, k):
                orig = nums[i:i+k]
                target = s[i:i+k]
                
                # Convert to fixed-width bytes (3 bytes per integer since nums[i] <= 10^5)
                # This enables Python's ultra-fast C-level substring search in O(k) time.
                orig_bytes = b"".join(x.to_bytes(3, 'big') for x in orig)
                target_bytes = b"".join(x.to_bytes(3, 'big') for x in target)
                
                if target_bytes not in (orig_bytes + orig_bytes):
                    valid = False
                    break
            
            if valid:
                ans += k
                
        return ans