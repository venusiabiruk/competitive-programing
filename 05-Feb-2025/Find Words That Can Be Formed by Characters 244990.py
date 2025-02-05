# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0
        d_chars = Counter(chars)
        for word in words:
            d_word = Counter(word)
            for key in d_word:
                if key not in d_chars or d_chars[key] < d_word[key]:
                    break
            else:
                s += len(word)
                
        return s

        


        