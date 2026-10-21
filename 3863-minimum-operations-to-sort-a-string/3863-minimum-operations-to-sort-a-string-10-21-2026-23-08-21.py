class Solution:

  def minOperations(self, s: str) -> int:
    if s == "".join(sorted(s)):
      return 0
    if len(s) == 2:
      return -1

    mn, mx = min(s), max(s)

    # 1 operation if min is at the start or max is at the end
    if s[0] == mn or s[-1] == mx:
      return 1

    # 2 operations if min or max appears in the interior
    if any(c in (mn, mx) for c in s[1:-1]):
      return 2

    return 3