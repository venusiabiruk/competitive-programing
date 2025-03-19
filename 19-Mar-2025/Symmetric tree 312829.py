# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        def symetry(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            if left.val == right.val:
                return symetry(left.left,right.right) and symetry(left.right,right.left)
        return symetry(root.left,root.right)

            
        

        