# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)  
        s2_count = Counter(s2[:len(s1)])  
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1 
            s2_count[s2[left]] -= 1  
            
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]] 
            
            left += 1  
            
            if s1_count == s2_count:
                return True
        
        return False



        