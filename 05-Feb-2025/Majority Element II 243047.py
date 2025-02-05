# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        n = len(nums)
        result = []
        for key in d:
            if d[key] > n/3:
                result.append(key)
        return result 