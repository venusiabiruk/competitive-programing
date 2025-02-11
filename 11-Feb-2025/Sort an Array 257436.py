# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        min_num = min(nums)
        count = [0] *((max_num - min_num)+1)
        result = []
        for num in nums:
            count[num-min_num] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                result.append(i+min_num)
        return result
         





       