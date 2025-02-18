# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def flip(index):
            for k in range(0,index//2 +1):
                arr[k], arr[index-k] = arr[index-k],arr[k]

        for i in range(len(arr)-1,0,-1):
            for j in range(1,i+1):
                if arr[j] == i+1:
                    flip(j)
                    res.append(j+1)
                    break
            flip(i)
            res.append(i+1)
        return res
                  
        