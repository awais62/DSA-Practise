class Solution:

    def solve(self , index ,nums ,  total , subset , res , target):
        
        if total == target:
            res.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return

        Sum = total + nums[index] 
        subset.append(nums[index])

        self.solve(index , nums , Sum , subset , res , target)

        Sum = total
        subset.pop()

        self.solve(index+1 , nums , Sum , subset , res , target)
          
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve(0,candidates ,0,[],res , target)
        return res