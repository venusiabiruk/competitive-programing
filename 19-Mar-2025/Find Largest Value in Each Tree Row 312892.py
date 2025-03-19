# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        rows = deque([root])
        while rows:
            row_max = rows[0].val
            for i in range(len(rows)):
                node = rows.popleft()
                row_max = max(row_max,node.val)
                if node.left:
                    rows.append(node.left)
                if node.right:
                    rows.append(node.right)
            res.append(row_max)
        return res
