class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(index , subset):
            if index >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            recursion(index+1 , subset)
            subset.pop()
            recursion(index+1 , subset)
        recursion(0,[])
        return res