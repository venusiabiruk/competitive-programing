# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        result = defaultdict(list)
        for key in d:
            if d[key] == 2:
                result[2].append(key)
            
        
        return result[2]
        