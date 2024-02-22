# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # handle if root is empty it can be used for case 1
        if not root:
            return root
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            # case 2
            if not root.right :
                return root.left
            elif not root.left:
                return root.right
            # case 3
            curr = root.right
            while curr.left:
                curr= curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
        return root

