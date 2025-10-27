# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = {}
       
        for i in arr:
            r = i % k
            f[r] = f.get(r, 0) + 1
        
        for r, count in f.items():
            if r == 0:  
                if count % 2 != 0:
                    return False
            elif k % 2 == 0 and r == k // 2:  
                if count % 2 != 0:
                    return False
            else:
                if f.get(k - r, 0) != count:
                    return False
        
        return True
