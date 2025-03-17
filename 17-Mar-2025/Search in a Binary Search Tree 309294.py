# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: 
        def search(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val > val:
                return search(node.left)
            elif node.val < val:
                return search(node.right)
        return search(root)

        