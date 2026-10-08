class Solution:

  def myAtoi(self, s: str) -> int:
    # 1. Ignore leading whitespace
    s = s.lstrip()
    if not s:
      return 0

    sign = 1
    i = 0
    n = len(s)

    # 2. Determine sign
    if s[0] == '-':
      sign = -1
      i += 1
    elif s[0] == '+':
      i += 1

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)
    res = 0

    # 3. Read valid numerical digits
    while i < n and s[i].isdigit():
      digit = ord(s[i]) - ord('0')

      # 4. Handle 32-bit integer rounding / overflow early
      if res > INT_MAX // 10 or (
          res == INT_MAX // 10 and digit > INT_MAX % 10
      ):
        return INT_MAX if sign == 1 else INT_MIN

      res = res * 10 + digit
      i += 1

    return sign * res