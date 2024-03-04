class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def dfs(level,root,res,leftToRight):
            if root is None:
                return
            if len(res)==level:
                res.append(deque([]))
            if leftToRight:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
            dfs(level+1,root.left,res,not leftToRight)
            dfs(level+1,root.right,res,not leftToRight)    
        dfs(0,root,res,True)
        return res