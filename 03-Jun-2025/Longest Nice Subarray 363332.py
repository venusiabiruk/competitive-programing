# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        window_or = 0
        max_length = 0
        for right in range(len(nums)):
            while (window_or & nums[right]) != 0:
                window_or ^= nums[left]
                left += 1
            window_or |= nums[right]
            max_length = max(max_length, right - left + 1)
        return max_length
        