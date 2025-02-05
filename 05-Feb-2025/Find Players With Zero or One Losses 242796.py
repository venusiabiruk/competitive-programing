# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l = []
        result = [[],[]]
        for arr in matches:
            l.append(arr[1])
        d = Counter(l)
        for arr in matches:
            if (arr[0] not in d) and (arr[0] not in result[0]):
                result[0].append(arr[0])
        for key in d:
            if d[key] ==1:
                result[1].append(key)
        result[0].sort()
        result[1].sort()
        

        return result

            
        
            

                
        
                
