class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""]*(n*2)
        result = []            
        self.bt(0,0,brackets,result)
        return result

    def bt(self , index , total , brackets , result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return

        if total > len(brackets)//2:
            return

        if total <0:
            return 

        brackets[index] = "("
        Sum = total + 1
        self.bt(index + 1 , Sum , brackets , result)
        
        brackets[index] = ")"
        Sum = total - 1
        self.bt(index + 1 , Sum , brackets , result)

