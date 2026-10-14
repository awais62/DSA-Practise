class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        curr_sum = sum
        
        for i in range(num):
            rem_slots = num - 1 - i
            min_d = max(0, curr_sum - 9 * rem_slots)
            
            # Leading zeros are not allowed for positive integers of length > 1
            if i == 0 and num > 1:
                min_d = max(min_d, 1)
                
            max_d = min(9, curr_sum)
            
            if min_d > max_d:
                return ""
            
            # Greedily pick the maximum possible valid digit
            d = max_d
            res.append(str(d))
            curr_sum -= d
            
        return "".join(res)