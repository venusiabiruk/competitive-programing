# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = defaultdict(list)
        min_in = float("inf")
        for i in range(len(list1)):
            if list1[i] in list2:
                index_s = i + list2.index(list1[i])
                result[index_s].append(list1[i])
        for i in result:
            min_in = min(i,min_in)
        return result[min_in]

       

        


 