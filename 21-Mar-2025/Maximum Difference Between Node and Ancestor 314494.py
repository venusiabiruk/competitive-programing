# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        def helper(cur, cur_min,cur_max):
            nonlocal result
            if not cur:
                return 
            result = max(abs(cur_max-cur.val),abs(cur_min-cur.val),result)
            cur_min = min(cur_min,cur.val)
            cur_max = max(cur_max,cur.val)
            
            helper(cur.left,cur_min,cur_max)
            helper(cur.right,cur_min,cur_max)
            return result
        return helper(root,root.val,root.val)



        