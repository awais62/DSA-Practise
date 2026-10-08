class Solution:

  def isMatch(self, s: str, p: str) -> bool:
    memo = {}

    def dp(i: int, j: int) -> bool:
      if (i, j) in memo:
        return memo[(i, j)]

      # If pattern is fully consumed, match is true only if s is also fully consumed
      if j == len(p):
        return i == len(s)

      # Check if current character matches or if '.' is present
      first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

      # Handle '*' operator
      if j + 1 < len(p) and p[j + 1] == '*':
        # Option 1: Treat x* as matching 0 elements -> skip 'x*' (advance pattern pointer by 2)
        # Option 2: Treat x* as matching 1+ elements -> consume 1 char from s if first_match is True
        ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
      else:
        # Standard single character match -> advance both pointers
        ans = first_match and dp(i + 1, j + 1)

      memo[(i, j)] = ans
      return ans

    return dp(0, 0)