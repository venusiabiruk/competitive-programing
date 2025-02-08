# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        
       
        for path in paths:
            parts = path.split(" ")
            folder = parts[0]
            
            for file in parts[1:]:
                name, content = file.split("(")  
                content = content[:-1]  
                c[content].append(folder + "/" + name) 
            
        result = []
        
        
        for v in c.values():
            if len(v) > 1:  
                result.append(v)
        
        return result
