# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        d = defaultdict(int)
        running_sum = 0
        for num in nums:
            running_sum += num
            if running_sum%k == 0:
                count +=1
            if running_sum%k in d:
                count += d[running_sum%k]
            d[running_sum%k] +=1
        return count
            
        