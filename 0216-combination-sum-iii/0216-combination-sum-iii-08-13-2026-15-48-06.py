class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def bt(last , total , subset):

            if total == n and len(subset) == k:
                res.append(subset.copy())
                return
            if  total > n or  len(subset) > k:
                return  

            
            for i in range(last , 10):
                Sum = total + i
                subset.append(i)
                bt(i+1 ,Sum , subset )
                subset.pop()
        bt(1 , 0 , [])
        return res