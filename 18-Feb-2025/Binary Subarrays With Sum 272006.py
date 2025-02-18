# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum = 0
        map = defaultdict(int)
        
        map[0] = 1 
        for num in nums:
            sum += num
            
            if sum - goal in map:
                count += map[sum - goal]
            
           
            map[sum] += 1
        
        return count
        