# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_que = deque()
        max_que = deque()
        l = 0
        max_length = 0
        for r in range(len(nums)):
            while max_que and max_que[-1] < nums[r]:
                max_que.pop()
            max_que.append(nums[r])

            while min_que and min_que[-1] > nums[r]:
                min_que.pop()
            min_que.append(nums[r])
            while max_que[0] - min_que[0] > limit:
                if nums[l] == max_que[0]:
                    max_que.popleft()
                if nums[l] == min_que[0]:
                    min_que.popleft()
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length