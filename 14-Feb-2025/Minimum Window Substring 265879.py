# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float(inf)
        t = Counter(t)
        window = Counter()
        ans = ""
        l = 0
        if len(s) < len(t):
            return ""
        def is_valid(window, t):
            for key in t:
                if window[key] < t[key]:
                    return False
            return True
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            while is_valid(window,t):
                if r-l+1 < min_len:
                    ans = s[l:r+1]
                    min_len = r-l+1
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
        return ans