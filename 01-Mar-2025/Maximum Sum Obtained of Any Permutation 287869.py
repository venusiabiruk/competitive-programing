# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        s = 0
        for start , end in requests:
            freq[start] +=1
            if end + 1 < n:
                freq[end + 1] -= 1
        for i in range(1,n):
            freq[i] = freq[i] + freq[i-1]
        nums.sort(reverse = True)
        freq.sort(reverse = True)
        result = 0
        for i in range(n):
            result = (result + nums[i] * freq[i])%(10**9 + 7)
        
        return result
        




        