# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.output = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        if curr:
            self.inorderTraversal(curr.left)
        
            self.output.append(curr.val)
            self.inorderTraversal(curr.right)
        return self.output
