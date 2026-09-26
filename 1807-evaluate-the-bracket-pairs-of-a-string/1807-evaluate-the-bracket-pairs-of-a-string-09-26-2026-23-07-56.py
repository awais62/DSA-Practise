class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge pairs into a hash map for O(1) lookups
        lookup = dict(knowledge)
        
        res = []
        key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(key)
                # Append mapped value if exists, otherwise '?'
                res.append(lookup.get(key_str, "?"))
                key = []
            elif in_bracket:
                key.append(char)
            else:
                res.append(char)
                
        return "".join(res)