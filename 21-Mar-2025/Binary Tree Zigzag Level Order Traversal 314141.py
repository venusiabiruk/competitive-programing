# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        temp = deque()
        temp.append(root)
        c = -1
        while temp:
            level = []
            for i in range(len(temp)):
                node = temp.popleft()
                if node:
                    level.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
            c +=1     
            if level and c%2 == 0:
                ans.append(level)
            if level and c%2 != 0:
                level.reverse()
                ans.append(level)
        return ans

        