class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # Only include '(' if it's inside a primitive string (depth > 0)
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                # Only include ')' if it remains inside a primitive string (depth > 0)
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)