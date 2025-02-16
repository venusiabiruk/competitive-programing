# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = Counter()
        
        for domains in cpdomains:
            n, s = domains.split()  
            n = int(n)
            s = s.split(".") 
            
            for i in range(len(s)):  
                sub = ".".join(s[i:])  
                result[sub] += n 
        
        return [f"{n} {s}" for s, n in result.items()]






        