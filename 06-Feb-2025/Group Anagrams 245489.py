# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            c = [0]*26
            for s in word:
                c[ord(s) - ord('a')] += 1
            key = tuple(c)
            result[key].append(word)
        return list(result.values())


        