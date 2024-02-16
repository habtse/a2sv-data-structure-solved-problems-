class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        ls =[]
        for i in paths:
            if i == '..' :
                if ls:                
                    ls.pop()
            elif i !='.' and i :
                ls.append(i)
        return '/'+ '/'.join(ls)
