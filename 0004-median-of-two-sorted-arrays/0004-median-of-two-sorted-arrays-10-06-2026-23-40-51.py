class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to achieve O(log(min(m, n))) complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            # Edge boundaries for nums1
            a_left = nums1[i - 1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < m else float("inf")

            # Edge boundaries for nums2
            b_left = nums2[j - 1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < n else float("inf")

            # Correct partition found
            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2 == 1:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
            elif a_left > b_right:
                # Too many elements chosen from nums1
                high = i - 1
            else:
                # Too few elements chosen from nums1
                low = i + 1

        return 0.0