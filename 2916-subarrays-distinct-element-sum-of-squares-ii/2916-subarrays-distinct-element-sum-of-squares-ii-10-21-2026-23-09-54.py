class SegmentTree:

  def __init__(self, n):
    self.n = n
    self.MOD = 10**9 + 7
    self.tree_sq = [0] * (4 * n)
    self.tree_sum = [0] * (4 * n)
    self.lazy = [0] * (4 * n)

  def _push(self, node, l, r):
    if self.lazy[node] != 0:
      val = self.lazy[node]
      mid = (l + r) // 2
      left, right = 2 * node, 2 * node + 1

      # Update left child
      len_left = mid - l + 1
      self.tree_sq[left] = (
          self.tree_sq[left]
          + 2 * val * self.tree_sum[left]
          + val * val * len_left
      ) % self.MOD
      self.tree_sum[left] = (self.tree_sum[left] + val * len_left) % self.MOD
      self.lazy[left] = (self.lazy[left] + val) % self.MOD

      # Update right child
      len_right = r - mid
      self.tree_sq[right] = (
          self.tree_sq[right]
          + 2 * val * self.tree_sum[right]
          + val * val * len_right
      ) % self.MOD
      self.tree_sum[right] = (self.tree_sum[right] + val * len_right) % self.MOD
      self.lazy[right] = (self.lazy[right] + val) % self.MOD

      self.lazy[node] = 0

  def update(self, node, l, r, ql, qr, val):
    if ql > r or qr < l:
      return
    if ql <= l and r <= qr:
      length = r - l + 1
      self.tree_sq[node] = (
          self.tree_sq[node] + 2 * val * self.tree_sum[node] + val * val * length
      ) % self.MOD
      self.tree_sum[node] = (self.tree_sum[node] + val * length) % self.MOD
      self.lazy[node] = (self.lazy[node] + val) % self.MOD
      return

    self._push(node, l, r)
    mid = (l + r) // 2
    self.update(2 * node, l, mid, ql, qr, val)
    self.update(2 * node + 1, mid + 1, r, ql, qr, val)

    self.tree_sq[node] = (self.tree_sq[2 * node] + self.tree_sq[2 * node + 1]) % self.MOD
    self.tree_sum[node] = (
        self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]
    ) % self.MOD

  def query_total_sum(self):
    return self.tree_sq[1]


class Solution:

  def sumCounts(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    seg = SegmentTree(n)
    last_pos = {}
    total_sum = 0

    for j in range(n):
      val = nums[j]
      prev = last_pos.get(val, -1)
      # Update range [prev + 1, j] by adding 1 to distinct counts
      seg.update(1, 0, n - 1, prev + 1, j, 1)
      last_pos[val] = j
      total_sum = (total_sum + seg.query_total_sum()) % MOD

    return total_sum