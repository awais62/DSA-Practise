class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = 0
        unmatched_close = 0

        for char in s:
            if char == "(":
                unmatched_open += 1
            else:
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    unmatched_close += 1

        return unmatched_open + unmatched_close