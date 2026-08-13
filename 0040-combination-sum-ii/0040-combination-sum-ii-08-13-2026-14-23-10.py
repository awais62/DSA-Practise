class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        
        n = len(nums)
        res = []
        def bt(index , total , subset):
            if total == 0 :
                res.append(subset.copy())
                return
            if total < 0 :
                return 

            for i in range(index  , n):
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                Sum = total - nums[i]
                bt(i+1 , Sum , subset)
                subset.pop()

        bt(0 , target , [] )
        return res