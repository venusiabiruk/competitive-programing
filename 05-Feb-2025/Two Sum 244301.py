# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for n , num  in enumerate(nums):
            if target - num in map:
                return ([map[target - num] , n ])
            elif num not in map:
                map[num] = n