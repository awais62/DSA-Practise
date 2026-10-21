class Solution:

  def maxAlternatingSum(self, nums: List[int]) -> int:
    # Compute squares and sort in descending order
    squares = sorted([x * x for x in nums], reverse=True)

    n = len(nums)
    # Number of positive positions (indices 0, 2, 4, ...)
    p = (n + 1) // 2

    # Sum the largest squares for positive positions and subtract the rest for negative positions
    return sum(squares[:p]) - sum(squares[p:])