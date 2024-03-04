# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = [float('-inf')]
        def checkValidity(root):
            nonlocal lst

            if root:
                val1 = checkValidity(root.left)
                if root.val <= lst[-1]:
                    return False
                lst.append(root.val)
                val2 = checkValidity(root.right)
                return val1 and val2
            return True
        return checkValidity(root)

        
        # if not root:
        #     return True
        # ancestor = root.val
        # if (root.left and root.left.val >= ancestor) or (root.right and ancestor >= root.right.val):
        #     return False
       
        # return self.isValidBST(root.left)==self.isValidBST(root.right)
        
        