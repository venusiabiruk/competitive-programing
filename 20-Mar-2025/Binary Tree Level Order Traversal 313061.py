# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = deque()
        temp.append(root)
        ans = []
        while temp:
            level = []
            for i in range(len(temp)):
                node = temp.popleft()
                if node:
                    level.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
            if level:
                ans.append(level)
        return ans
        
        

            
            
            

        