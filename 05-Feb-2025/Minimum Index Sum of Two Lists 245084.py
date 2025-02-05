# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_s = float("inf")
        for n, word in enumerate(list1):
            if word in list2:
                index_s = n + list2.index(list1[n])
                if min_s > index_s:
                    min_s = index_s
                    result = [word]
                elif min_s == index_s:
                    result.append(word)
        return result

       

        


 