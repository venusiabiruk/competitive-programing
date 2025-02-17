# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        map = defaultdict(int)
        
        map[0] = 1 
        for num in nums:
            sum += num
            
            if sum - k in map:
                count += map[sum - k]
            
           
            map[sum] += 1
        
        return count
