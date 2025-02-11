# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        result = []
        max_v = max(nums)
        min_v = min(nums)
        count = [0]*((max_v - min_v) +1)
        for num in nums:
            count[num - min_v] += 1
        for i in range(len(count)):
            for _ in range(count[i]):
                result.append(i+min_v)
        return result



