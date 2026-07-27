class Solution:
    def validStrings(self, n: int) -> List[str]:
        numbers = ["0"]*n
        res = []

        def BT(index,flag,numbers,res):
            if index >= len(numbers):
                res.append ("".join(numbers))
                return

            numbers[index]="1"
            BT (index+1 , True , numbers , res)

            numbers[index] = "0"
            if flag == True:
                BT(index+1,False,numbers,res)
                numbers[index] = '1'

        BT(0,True,numbers,res)
        return res
                