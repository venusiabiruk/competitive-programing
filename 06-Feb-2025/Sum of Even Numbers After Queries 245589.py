# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        r = []
        se = sum(num for num in nums if num %2 == 0)
        for arr in queries:
            if nums[arr[1]] % 2 == 0:
                se -= nums[arr[1]]
            nums[arr[1]] += arr[0]

            if nums[arr[1]] % 2 == 0:
                se += nums[arr[1]]
            r.append(se)
        return r


            



        