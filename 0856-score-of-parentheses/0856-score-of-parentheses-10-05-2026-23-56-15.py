class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                # If we find a primitive "()", its value is 2^depth
                if s[i - 1] == '(':
                    ans += 1 << depth
                    
        return ans