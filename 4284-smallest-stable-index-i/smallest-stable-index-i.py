class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [nums[-1]] * n
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        prefix_max = 0
        for i, value in enumerate(nums):
            prefix_max = max(prefix_max, value)

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1