# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d ={}
        l = []
        d["first"] = "qwertyuiop"
        d["second"] = "asdfghjkl"
        d["third"] = "zxcvbnm"
        
        for word in words:
            small_letter = word.lower()
            
            if all(c in d["first"] for c in  small_letter):
                l.append(word)
            elif  all(c in d["second"] for c in  small_letter):
                l.append(word)
            elif  all(c in d["third"] for c in  small_letter):
                l.append(word)
        return l




