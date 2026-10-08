class Solution:

  def threeSumClosest(self, nums: list[int], target: int) -> int:
    nums.sort()
    closest_sum = float('inf')
    n = len(nums)

    for i in range(n - 2):
      # Skip duplicate values for the first element to optimize
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, n - 1

      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        # Exact target match is the closest possible sum
        if current_sum == target:
          return current_sum

        # Update closest sum if current_sum is closer to target
        if abs(target - current_sum) < abs(target - closest_sum):
          closest_sum = current_sum

        # Move pointers based on comparison with target
        if current_sum < target:
          left += 1
        else:
          right -= 1

    return closest_sum