# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def helper(node,num):
            if not node:
                return 
            if not node.left and not node.right:
                arr.append(num*10 +node.val)
                return
            num = num*10 + node.val
            helper(node.left,num)
            helper(node.right,num)
            
        helper(root,0)
        return sum(arr)




            




            


            




        