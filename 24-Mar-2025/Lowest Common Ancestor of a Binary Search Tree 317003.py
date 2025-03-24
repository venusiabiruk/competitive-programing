# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node,target):
            if node.val == target:
                return [node]
            ans=[node]
            if node.val > target:
                ans.extend(helper(node.left,target))
            else:
                ans.extend(helper(node.right,target))
            return ans

        first = helper(root,p.val)
        second = set(helper(root, q.val))
        for node in first[::-1]:
            if node in second:
                return node

      
      
            

        