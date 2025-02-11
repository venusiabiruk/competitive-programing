# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

 nums.sort()
        r = []
        for i in range(len(nums)):
            if nums[i] == target:
                r.append(i)
        return r
                