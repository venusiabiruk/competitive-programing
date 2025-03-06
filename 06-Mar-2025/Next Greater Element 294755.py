# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {num:-1 for num in nums2}
        dec_stack = []
        for num in nums2:
            while dec_stack and dec_stack[-1] < num:
                top = dec_stack.pop()
                next_greater[top] = num
            dec_stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = next_greater[nums1[i]]
        return nums1


        


        