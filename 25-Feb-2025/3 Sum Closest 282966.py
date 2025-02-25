# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        c_sum = float(inf)
        for i in range(n):
            lo , hi = i+1, n-1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target-cur_sum) < abs(target-c_sum):
                    c_sum = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi-=1
        return c_sum 



        