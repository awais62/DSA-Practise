class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dictionary = {}
        for num in nums:


            if num in dictionary:
                dictionary[num] += 1
            else :
                dictionary[num] = 1
        
            if dictionary[num] > n//2:
                return num
            